# Install every skill in .\skills into Claude Code and Codex (Windows).
# Uses a directory junction, so edits in this repo go live. Pass -Copy to copy instead.
param([switch]$Copy)
$ErrorActionPreference = 'Stop'
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$targets = @((Join-Path $HOME '.claude\skills'), (Join-Path $codexHome 'skills'))
foreach ($target in $targets) {
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    foreach ($skill in Get-ChildItem -Directory (Join-Path $PSScriptRoot 'skills')) {
        $dest = Join-Path $target $skill.Name
        $existing = Get-Item -LiteralPath $dest -Force -ErrorAction SilentlyContinue
        if ($existing) {
            # A junction must be removed on its own: Remove-Item -Recurse on a junction in
            # Windows PowerShell 5.1 can delete the files in the repo it points to.
            if ($existing.Attributes -band [IO.FileAttributes]::ReparsePoint) { [IO.Directory]::Delete($dest) }
            else { Remove-Item -LiteralPath $dest -Recurse -Force }
        }
        if ($Copy) { Copy-Item -Recurse $skill.FullName $dest }
        else { New-Item -ItemType Junction -Path $dest -Target $skill.FullName | Out-Null }
        Write-Output "installed $($skill.Name) -> $dest"
    }
}
