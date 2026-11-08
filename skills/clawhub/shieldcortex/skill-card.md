## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ShieldCortex with AI agents to retain and recall useful context across sessions, organize it as a knowledge graph, and scan memory or agent inputs for security threats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this skill suspicious because it reports unpinned package execution and setup behavior that can access agent configuration and change hook files beyond the declared scope; scanner coverage was partial.

Mitigation: Before installing, verify the package execution and the files affected by setup and startup behavior; avoid installation until those changes are understood.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance, Configuration instructions]

**Output Format:** [Natural language and structured memory or security scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recalled context, knowledge graph results, security findings, or setup guidance.]

## Skill Version(s):

5.18.2 (source: server-resolved release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
