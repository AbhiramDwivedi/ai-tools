# What a schema does not check

Last week a listing went live at $38,900 for a lamp. The model had returned a perfectly well-formed object, and our schema passed it, because the schema only knew that `price_cents` was an integer.

That is the whole contract. A JSON schema makes the model fill the right fields with the right types. It cannot tell you whether the values make sense, and nothing in the response will warn you when they don't.

So we added a second check in code: prices outside three times the category median go to a review queue instead of the storefront. It caught four bad listings in the first two days, all of them off by a factor of a hundred because the model had mixed up cents and dollars. I would not ship structured output to production without a check like that, and I'd write it before the prompt.
