# Security scope — 0.1.30

Reviewed 2026-09-13: source, generated runtime, dependency lock, network/auth
boundaries, redaction, paid-request retries, cleanup reporting and release inventory.
Offline regression tests use synthetic credentials and mocked transports, never real attacks.

## Controls

- No runtime dependencies, package lifecycle install hooks, shell execution,
  wallet/chain signing, local RPC adapters or arbitrary local-file uploads.
- On-demand accepts only `https://ondemand.thetaedgecloud.com` as an origin.
  Dedicated inference accepts HTTPS subdomains of thetaedgecloud.com or
  onthetaedgecloud.com. Credentials, nonstandard ports, paths, queries and
  fragments in configured origins are rejected. All transports refuse redirects.
- 0.1.30: code-enforced confirmation. The runtime refuses all 23 resource-mutating commands
  (deployments, GPU nodes, RAG agents/documents, video, Characters create/update/delete/
  session lifecycle) outside dry-run unless `confirm:true`. The `theta()` facade exposes
  read-only helpers only. Video inference (seedance and other video services) also requires `confirm:true`. Chat (max_tokens ≤ 5000), image/audio inference, upload-URL creation and in-session Characters messages stay usage-billed and ungated.
- 0.1.29 hosted-MCP client: one fixed origin (`https://controller.thetaedgecloud.com/mcp`),
  project key only in `x-api-key`, redirects refused, never retried. GPU create/start/
  stop/delete require `confirm:true` and honour dry-run. Create requires a provider-side
  `max_price_per_hour_usd` cap and refuses before provisioning when the listed price exceeds it.
- Tools are rejected for chat models that silently drop them (Qwen3.8, Ling), so a
  plain-text answer is never mistaken for a tool-aware run.
- Resource path components are encoded; empty/dot/control-character IDs rejected.
- Mutating/billable HTTP requests are single-attempt. GETs alone may retry.
- Dry-run runtime results and structured error secrets are fully redacted, not
  partially revealed. Named password/key environment entries are redacted too.
- Malformed or unterminated event streams fail rather than claim successful output.
- Disposable deployment verification reports operation/cleanup failures together;
  unknown handles/list shapes never prove deletion. Reconcile remote resources manually
  after an ambiguous create timeout; cleanup cannot be guaranteed without a returned ID.

## Trust and limits

This is a trusted-operator API library, not a sandbox or a spending firewall.
Calling the library directly bypasses agent-level approval workflows; environment
credentials confer their provider permissions. Use least-privilege project/game keys,
provider-side quotas, protected secret storage and explicit approval for paid writes.
Dry-run is opt-in and still permits reads. Model-generated tool calls are returned
as data, never executed; independently validate/authorize their arguments.

Theta-managed DNS/TLS and provider APIs remain trusted. User-authorized remote
media/webhook URLs are forwarded to Theta, not locally fetched by this library.
Outputs can contain user content or signed media URLs: treat them as private and
untrusted; redaction is not a guarantee against arbitrary unlabelled secret text.
Do not log complete provider responses or publish customer inputs.

Automated scans and manual review reduce risk but cannot establish absolute security.
No intrusive provider penetration test, production GPU creation/deletion, video
mutation or game-key character session was performed for the security release.
