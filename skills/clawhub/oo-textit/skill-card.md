## Description:

Operate TextIt through an OOMOL-connected account to read, create, update, and delete TextIt contacts, groups, messages, broadcasts, and workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TextIt via the OOMOL-connected oo CLI, including contact and group management, message and broadcast listing, and sending messages or broadcasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute unverified code from the internet.

Mitigation: Review the installer source before use and prefer a signed, versioned, or package-manager installation path with verification.

Risk: Write and destructive TextIt actions can change or delete TextIt contacts, groups, messages, or broadcasts.

Mitigation: Confirm exact targets, payloads, and expected effects with the user before running write or destructive actions.

## Reference(s):

- [TextIt homepage](https://textit.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-textit)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
