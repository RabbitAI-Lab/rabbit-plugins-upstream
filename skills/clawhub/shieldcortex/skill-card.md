## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ShieldCortex to give AI agents persistent semantic memory and knowledge-graph recall. They can also use its security scanning and memory-firewall features to detect and enforce against prompt injection, credential leaks, and memory poisoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabled hooks can automatically resolve and run packages through npx, and gateway self-heal can delete legacy hook directories without backups.

Mitigation: Back up legacy hook directories, disable self-heal before enabling hooks, and use reviewed, pinned local packages.

Risk: Captured memories may contain sensitive content, and enabling Cloud sync or webhooks can transfer data outside the local environment.

Mitigation: Review captured memories and enable Cloud sync or webhooks only when you accept the disclosed data transfers.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex release notes](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Memory entries, security scan findings, and setup guidance with CLI and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory is stored locally by default; Cloud sync is opt-in.]

## Skill Version(s):

5.17.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
