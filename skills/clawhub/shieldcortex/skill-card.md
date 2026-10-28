## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using supported AI agent hosts use ShieldCortex to retain and recall project context, organize knowledge, and scan memories and agent inputs for prompt injection and credential risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The enabled background integration can run downloaded software and delete legacy integration files without a backup.

Mitigation: Before enabling the OpenClaw hook, disable automatic self-healing, back up legacy hook directories, review package versions, and prevent runtime package fetching; preinstallation alone does not guarantee offline operation.

Risk: Automatic memory capture can retain conversation content, and selected memories can be uploaded when cloud sync is enabled.

Mitigation: Review captured memories and cloud-upload settings before use, and enable cloud sync only after reviewing what it will transmit.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd)
- [Security audit waivers](https://github.com/Drakon-Systems-Ltd/ShieldCortex/blob/main/docs/security/audit-waivers.md)
- [Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command examples and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Version-specific setup and operation guidance for supported AI agent hosts.]

## Skill Version(s):

5.15.3 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
