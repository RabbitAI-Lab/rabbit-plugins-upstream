## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ShieldCortex to give AI agents persistent local memory, retrieve related knowledge, and scan or enforce protections against prompt injection, credential leaks, and poisoned content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabled hooks may automatically download and run unpinned packages, and the gateway self-heal may delete legacy hook folders without backups.

Mitigation: Provision reviewed exact package versions and prevent runtime npm downloads. Set SHIELDCORTEX_SKIP_SELF_HEAL=1 before starting the gateway, and back up customized legacy hooks.

Risk: Captured memories may contain sensitive information, and cloud sync can share memory contents.

Mitigation: Review captured memories and leave cloud sync disabled unless you intend to share their contents.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex website](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides setup and use instructions for memory, scanning, and agent integrations.]

## Skill Version(s):

5.17.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
