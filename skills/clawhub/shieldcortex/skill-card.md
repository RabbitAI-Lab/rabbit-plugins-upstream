## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to add persistent local memory, semantic recall, knowledge graph workflows, and security checks around memory writes, agent instructions, and tool outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ShieldCortex is a high-access local memory and security layer that can read agent transcripts and configuration files and store selected content in ~/.shieldcortex.

Mitigation: Install it only for workflows that need persistent local memory and security scanning; periodically review local audit and memory contents.

Risk: Auto-memory and hook self-heal behavior can be broader than some workflows expect.

Mitigation: Disable auto-memory or self-heal when those behaviors are too broad for the environment.

Risk: Cloud sync can transmit selected memory or audit data when intentionally enabled.

Mitigation: Keep cloud sync off unless sync is required, and enable it only with an explicit API key and review of the data-sharing posture.

## Reference(s):

- [ShieldCortex ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface local memory context, audit summaries, scan results, setup commands, and configuration guidance.]

## Skill Version(s):

4.51.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
