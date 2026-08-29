## Description:

Guides agents through Dgate CLI or MCP onboarding, governed enterprise data discovery, security-policy inspection, and bounded read-only queries through Alibaba Cloud Agent Data Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect an agent to Alibaba Cloud Dgate, inspect identity and instance permissions, discover governed enterprise data resources, retrieve DataWiki semantics, and run authorized read-only queries. It is for read-only inspection and access workflows, not data mutation, DMS change orders, direct database connections, or permission changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an agent to Dgate can involve credential generation, CLI installation, or instance authorization changes.

Mitigation: Confirm the Region and target instance, grant least-privilege read access, and require explicit user approval before installation, identity creation, credential generation, or permission grants.

Risk: Dgate AccessTokens or one-time install commands may be exposed if copied into chat, logs, URLs, screenshots, or source files.

Mitigation: Keep DGATE_ACCESS_TOKEN and token-bearing install commands out of prompts, source files, logs, URLs, and screenshots; configure secrets only through encrypted runtime settings.

Risk: Metadata visibility, datasource visibility, or platform administrator status can be mistaken for SQL access.

Mitigation: Check real instance-level permissions with Dgate ACL surfaces before querying, and report that catalog visibility or admin status is not proof of query authorization.

Risk: Queries could return sensitive or excessive data if the workflow is not bounded.

Mitigation: Use only read-only statements, prefer explicit columns and restrictive predicates, keep row limits small, and stop on policy-blocked statuses rather than retrying or overriding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-aidbs-dgate-skill)
- [Dgate Quick Start](https://dgate.dms.aliyun.com/quick-start)
- [Dgate Quick Start for cn-hangzhou](https://dgate.dms.aliyun.com/quick-start?region=cn-hangzhou)
- [Dgate public installer for macOS and Linux](https://d.tb.cn/i.sh)
- [Dgate public installer for Windows PowerShell](https://d.tb.cn/i.ps1)
- [Install Dgate and create an Agent identity](references/getting-started.md)
- [Dgate MCP tools](references/mcp-tools.md)
- [Dgate CLI routing](references/cli-routing.md)
- [DataWiki workflow](references/datawiki.md)
- [Resource discovery](references/resource-discovery.md)
- [Identity, authorization, and security](references/identity-and-security.md)
- [RAM permissions](references/ram-policies.md)
- [Error recovery](references/error-recovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown responses with inline shell commands and structured status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow guidance with request IDs, exact target identifiers, policy notices, and explicit approval boundaries when external state could change.]

## Skill Version(s):

0.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
