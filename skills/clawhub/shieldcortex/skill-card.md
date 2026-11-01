## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

AI agent users and developers use ShieldCortex for persistent searchable memory and to scan or filter memory and agent content for injection and credential risks. It provides enforcing hooks on supported hosts and an MCP memory server on other integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: On hosts with the OpenClaw memory hook enabled, missing dependencies can be resolved through npx, which may download and run packages automatically.

Mitigation: Review the exact executable releases, use reviewed local dependencies, and prevent hook-time downloads.

Risk: Captured memories persist locally, and enabling cloud sync or webhooks can share their payloads externally.

Mitigation: Review captured memories and leave cloud sync and webhooks disabled unless you intend to share their payloads.

Risk: The OpenClaw hook can perform automatic self-heal file changes at gateway startup.

Mitigation: Back up customized legacy hooks and set SHIELDCORTEX_SKIP_SELF_HEAL=1 before gateway startup if you want self-heal to be warn-only.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex product site](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd)
- [ShieldCortex ClawHub release](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration]

**Output Format:** [Text responses, scan reports, and shell command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses vary by memory, query, or scan; no fixed output size is specified.]

## Skill Version(s):

5.17.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
