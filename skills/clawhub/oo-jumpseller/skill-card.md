## Description:

Jumpseller (jumpseller.com) skill for reading, creating, and updating store data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External store operators and developers use this skill to retrieve, search, create, and update Jumpseller store entities through the OOMOL oo CLI. It is intended for connected Jumpseller accounts, with user confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup can execute a remote installer for the oo CLI.

Mitigation: Install the oo CLI through a verified, pinned, or package-manager method before using the skill.

Risk: Write actions can modify Jumpseller store data.

Mitigation: Review the exact payload and expected effect with the user before running create or update actions.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Jumpseller homepage](https://jumpseller.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
