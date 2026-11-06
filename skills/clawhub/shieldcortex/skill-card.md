## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using supported AI agent hosts use ShieldCortex to configure persistent memory and security scanning, then recall and manage stored context through agent integrations or command-line tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An enabled OpenClaw hook may resolve npm packages automatically when local binaries are unavailable, downloading and running software.

Mitigation: Review and install the required package versions locally, configure the hook to use those binaries, and prevent automatic download fallbacks.

Risk: The OpenClaw hook's bootstrap self-heal can delete legacy hook directories without making backups.

Mitigation: Back up legacy hook directories and set SHIELDCORTEX_SKIP_SELF_HEAL=1 before gateway startup when migration should remain read-only.

Risk: Captured memory can contain conversation context, and eligible memory content may be uploaded when cloud sync is enabled.

Mitigation: Review captured memories and keep cloud sync disabled unless you intend to upload eligible memory content.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with shell command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill artifact contains instructions and a manifest, not executable files.]

## Skill Version(s):

5.18.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
