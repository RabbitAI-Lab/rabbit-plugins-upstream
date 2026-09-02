## Description:

Builds runnable digital-employee workspaces from a business codebase, API documentation, or functional specification, including operating rules, persona files, MCP tools, generated workflow skills, and onboarding and verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaggerxzj](https://clawhub.ai/user/jaggerxzj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business-system owners use this skill to convert an existing business capability into a deployable agent workspace with explicit approval gates, MCP integration, workflow scripts, and harness onboarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated agents may receive business credentials and perform live API changes without enough operational safeguards.

Mitigation: Review the generated workspace before use, require least-privilege credentials, and make dry-run or explicit execute flags mandatory for write operations.

Risk: Scheduled heartbeat or cron execution can create unattended business actions if its scope and permissions are too broad.

Mitigation: Do not enable heartbeat or cron execution until cadence, data sources, allowed actions, and permissions are explicitly defined and reviewed.

Risk: Self-contained Pattern C workflows can retain unnecessary live API helpers that increase credential and side-effect exposure.

Mitigation: Remove API helpers for self-contained Pattern C workflows unless the user has explicitly approved a live runtime channel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jaggerxzj/skills/digital-employee-builder)
- [Server-resolved GitHub provenance](https://github.com/jaggerxzj/digital-employee-builder/tree/main/skills/digital-employee-builder)
- [Business-Code Modification Proposals](references/business-api-proposals.md)
- [Harness Adapters: Onboarding Outside OpenClaw](references/harness-adapters.md)
- [MCP Wrapping Essentials](references/mcp-integration.md)
- [OpenClaw Workspace Specification](references/openclaw-workspace.md)
- [Script Encapsulation of Business Code](references/script-encapsulation.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files, code templates, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a self-contained agent workspace with MCP server scaffolding, per-workflow skill files, approval gates, and verification checklists.]

## Skill Version(s):

0.1.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
