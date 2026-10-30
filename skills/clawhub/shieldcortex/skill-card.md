## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain searchable memory across sessions and scan or filter agent inputs, stored memories, and tool outputs for security threats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabled hooks may automatically download and run packages without a fixed version.

Mitigation: Review the runtime source, use reviewed local package versions, and prevent automatic registry fallback where practical.

Risk: Conversation capture can store sensitive content locally, and enabled cloud memory sync uploads selected saved memories.

Mitigation: Disable conversation capture for sensitive work and enable cloud sync only when you accept uploading saved memories.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Security audit waiver details](https://github.com/Drakon-Systems-Ltd/ShieldCortex/blob/main/docs/security/audit-waivers.md)
- [Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration, Shell commands]

**Output Format:** [Text and structured memory or security scan results, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on enabled integrations and enforcement settings.]

## Skill Version(s):

5.16.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
