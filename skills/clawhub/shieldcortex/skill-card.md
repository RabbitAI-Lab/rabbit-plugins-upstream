## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using supported AI-agent environments use ShieldCortex for persistent semantic memory and knowledge-graph recall, and to scan for prompt injection, credential leaks, and poisoned content. Enforcement capabilities vary by integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security plugin may ignore configured approval controls and allow some rejected writes through its gate.

Mitigation: Do not rely on it as a security gate until the approval-control defects are fixed; use reviewed, pinned local installations.

Risk: Automatic hook repair may overwrite existing hook files.

Mitigation: Back up existing hooks and set SHIELDCORTEX_SKIP_SELF_HEAL=1 before gateway startup.

Risk: Automatically captured conversation content persists locally, and enabled cloud sync can upload disclosed data.

Mitigation: Review auto-memory settings and enable cloud sync only when those uploads are intended.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Agent-readable memory context, security findings, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory is persistent; enforcement capabilities vary by agent integration.]

## Skill Version(s):

5.11.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
