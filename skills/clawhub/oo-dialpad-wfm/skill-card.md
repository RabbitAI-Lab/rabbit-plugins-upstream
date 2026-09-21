## Description:

Dialpad WFM provides read-only access to schedule entries, activity metrics, and agent metrics through an OOMOL-connected Dialpad WFM account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Dialpad WFM schedules and metrics through the OOMOL connector after inspecting the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run network-fetched installer scripts without verification.

Mitigation: Review the oo CLI installation path first; prefer an official versioned installer or inspect and verify the install script before running it.

Risk: The connector reads Dialpad WFM schedules and metrics through an OOMOL-connected account.

Mitigation: Connect only a Dialpad WFM account that the user intends OOMOL to use for schedule and metrics reads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dialpad-wfm)
- [Dialpad WFM homepage](https://www.dialpad.com/features/workforce-management-software/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions return Dialpad WFM data with execution metadata; setup guidance may include installer commands when the oo CLI is missing.]

## Skill Version(s):

1.0.4 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
