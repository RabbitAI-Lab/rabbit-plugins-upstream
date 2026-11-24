# Templates and substitutions

## Stored templates

`template/set` creates a template (no `id`) or updates one (`id` given) and returns it with its `id`;
`email/send` with `template_id` takes the subject, body, sender and other fields from the template, and the call
can still pass `recipients`, substitutions and any field to override.

```json
{
  "template": {
    "name": "Order confirmation",
    "editor_type": "html",
    "template_engine": "liquid",
    "subject": "Order {{ order.number }}",
    "from_email": "noreply@example.com",
    "from_name": "Example",
    "body": {"html": "<p>Hello, {{ name }}!</p>", "plaintext": "Hello, {{ name }}!"}
  }
}
```

Other methods: `template/get` (by id), `template/list` (`limit` / `offset`; fewer than `limit` items means the end),
`template/delete`.

## Open a template in the visual editor

A template created or updated through the API opens in the UniOne control panel editor at

```
https://cp.unione.io/en/templates/edit-body-html/<template_id>
```

After `template/set`, give the user this link (with the returned `id`) so they can review and polish the email
visually; in a coding agent you may open it in the browser when the user agrees. The user must be signed in to
the control panel with the account that owns the API key (a project template needs that project's account).
Read the result back with `template/get` before sending.

## Template engines

| Engine | Syntax | Use for |
|---|---|---|
| `simple` (default) | `{{name}}`, default `{{name|Customer}}`, condition `{{has_orders?Text}}` | Plain merge tags |
| `velocity` | `$name`, `$order.number`, `#if … #elseif … #else … #end`, `#foreach($i in $items) … #end` | Objects, arrays, logic |
| `liquid` | `{{ name }}`, `{{ order.number }}`, `{% if %}…{% else %}…{% endif %}`, `{% for i in items %}…{% endfor %}`, filters | Objects, arrays, logic |
| `none` | no processing | Content that contains `{{` or `$` literally |

Set it with `template_engine` in `email/send` / `template/set` (or the `X-UNIONE-Template-Engine` header,
which wins). The engine must match the syntax of the body: a Liquid body sent with the default `simple` engine
goes out with the raw tags. Full syntax: the email-templates skill and [https://docs.unione.io/en/web-api-ref](https://docs.unione.io/en/web-api-ref).

Substitution values: strings, numbers, and — for `velocity` and `liquid` — objects and arrays. Names: Latin letters,
digits and `_`, starting with a letter; names are case-sensitive.
