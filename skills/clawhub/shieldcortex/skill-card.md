## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent users use ShieldCortex to keep persistent memory, retrieve related context, and scan or guard agent memory and instruction workflows against unsafe content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unpinned package invocations, which may download packages when hooks run.

Mitigation: Review the package commands and pin or preinstall the required packages before enabling the described integrations.

Risk: The OpenClaw hook's bootstrap self-heal can copy hook files and remove named legacy hook directories automatically.

Mitigation: Review the affected paths and disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 if you do not want those automatic file changes.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex on npm](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)
- [ShieldCortex issue tracker](https://github.com/Drakon-Systems-Ltd/ShieldCortex/issues)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for installing and using a local memory and security tool; outputs depend on the user's agent setup and configuration.]

## Skill Version(s):

5.20.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
