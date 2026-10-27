## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use ShieldCortex to add persistent semantic memory and knowledge-graph recall, and to scan agent content for prompt injection, credential leaks, and poisoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gateway startup maintenance can delete old hook folders without backups, and the write manifest omits persistent integration changes.

Mitigation: Back up existing hook folders and agent settings before starting the gateway, consider setting SHIELDCORTEX_SKIP_SELF_HEAL=1, and review integration changes against the write manifest.

Risk: Automatic memory capture or Cloud sync can involve sensitive stored content.

Mitigation: Disable automatic memory capture for sensitive sessions and review stored content before enabling Cloud sync.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

5.15.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
