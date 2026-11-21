## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ShieldCortex to give AI agents persistent local memory and to scan or enforce protections against prompt injection, credential leaks, and poisoned content across supported integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reported unpinned `npx` commands may download and run packages during an enabled hook path.

Mitigation: Review the package names and versions before installation; preinstall trusted `shieldcortex` and `mcporter` binaries so the hook does not need to resolve them through `npx`.

Risk: The partial scan did not inspect executable files, so it cannot establish that all related components are safe.

Mitigation: Review the related npm package and executable components before enabling hooks, and complete a security review that covers those files.

## Reference(s):

- [ShieldCortex homepage](https://shieldcortex.ai)
- [npm package](https://www.npmjs.com/package/shieldcortex)
- [ClawHub release](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

5.20.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
