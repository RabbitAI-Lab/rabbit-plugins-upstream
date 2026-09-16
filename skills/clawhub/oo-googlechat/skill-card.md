## Description:

Google Chat lets an agent read Google Chat spaces and messages through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to retrieve Google Chat spaces, messages, and message history from an already connected account while keeping credentials server-side.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can direct a user or agent to run unverified remote installer scripts locally.

Mitigation: Prefer a verified package or pinned release with checksum or signature verification, and require explicit user approval before installing the oo CLI.

## Reference(s):

- [Google Chat](https://workspace.google.com/products/chat/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Chat Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-googlechat)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before building payloads; Google Chat action results are returned as JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
