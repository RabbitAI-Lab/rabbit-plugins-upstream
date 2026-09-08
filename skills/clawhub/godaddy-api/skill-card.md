## Description:

Work with GoDaddy's gddy CLI, public Domains MCP, REST and GraphQL APIs, domains and DNS, Commerce, Hosting, Email, experimental Platform apps, and Agent Name Service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[solarx56](https://clawhub.ai/user/solarx56)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to help agents discover current GoDaddy CLI, MCP, REST, and GraphQL workflows, authenticate appropriately, and prepare domain, DNS, hosting, email, and platform changes with verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward purchases, DNS edits, hosting changes, and other account mutations.

Mitigation: Require explicit approval for the exact resource, cost, environment, and proposed effect before mutation; use dry-run where available and verify state afterward.

Risk: Credential misuse could expose OAuth tokens, PATs, or account data.

Mitigation: Use scoped OAuth or PAT flows, never ask the user to paste tokens into chat, and avoid debug output around secrets.

Risk: Mutable or unverified installers can execute unexpected code.

Mitigation: Prefer the versioned official gddy release and verify the archive SHA-256 before extracting or executing it.

Risk: Retries of non-idempotent operations can duplicate records or repeat billed actions.

Mitigation: Branch on stable error codes, inspect current server state after ambiguous failures, and poll returned operation IDs instead of resubmitting writes.

## Reference(s):

- [GoDaddy API Skill on ClawHub](https://clawhub.ai/solarx56/skills/godaddy-api)
- [GoDaddy CLI, MCP, and agent platform](references/agent-platform.md)
- [Dynamic API catalog](references/api-catalog.md)
- [Mutation safety](references/safety.md)
- [Errors, retries, and limits](references/errors-and-limits.md)
- [GoDaddy CLI](https://github.com/godaddy/cli)
- [GoDaddy Domains MCP documentation](https://developer.godaddy.com/en/docs/api-users/mcp)
- [GoDaddy Domains v3 OpenAPI specification](https://developer.godaddy.com/openapi/domains-v3.json)
- [GoDaddy API rate limits](https://developer.godaddy.com/en/docs/api-users/rate-limits)
- [Agent Name Service registration reference](https://developer.godaddy.com/en/docs/references/rest/ans/registration)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve secrets, require approval for account mutations, and verify server state after changes.]

## Skill Version(s):

2.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
