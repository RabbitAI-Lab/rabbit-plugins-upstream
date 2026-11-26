# API keys and projects

- **Account key** (control panel → API): every method, including projects, the sandbox domain and confirmed emails.
- **Project key**: projects group domains, templates, webhooks and unsubscribe lists — e.g. one project per client.
  Every call with a project key sees only that project's data, and project keys cannot call `project/*`,
  `domain/get-sandbox-domain` or `confirmed-email/*`. `system/info` tells which key is used (`project_id` present
  means a project key).
- `project/create` returns the project's `api_key`: store it like any secret, it is shown in the API response.
- Keep keys server-side in `UNIONE_API_KEY` (or a secret store); never in browser or mobile code, never in git, never in
  logs. The API does not allow calls from browsers.
