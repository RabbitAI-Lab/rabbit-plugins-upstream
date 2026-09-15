## Description:

Use esa (esa.io) through the OOMOL-connected oo CLI to read, create, update, search, and delete esa content without handling raw credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external agents use this skill to operate esa workspaces through OOMOL's connector, including reading teams and posts, searching content, and creating or updating Markdown posts and comments. The skill also supports archival, rollback, deletion, and other state-changing content operations when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer commands locally.

Mitigation: Install the oo CLI only from trusted OOMOL documentation, prefer a pinned version, and verify checksums or signatures when available.

Risk: The skill can perform esa write and destructive actions such as creating, updating, rolling back, or deleting posts and comments.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

Risk: Connector schemas and payload requirements are resolved at runtime through the oo CLI.

Mitigation: Fetch the live action schema before constructing a payload and compare the payload against that schema before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esa)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [esa homepage](https://esa.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute esa read, write, or destructive actions through the oo CLI; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
