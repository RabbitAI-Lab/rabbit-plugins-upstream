## Description:

Enables agents to read, create, update, upload, favorite, and export Strava data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Strava account data through an agent, including athlete, activity, club, route, segment, equipment, and training workflows. It supports read actions, state-changing actions with confirmation, and setup recovery when authentication or connection errors occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the oo CLI installation source first, prefer official versioned downloads, and verify signatures or checksums before running installer commands.

Risk: State-changing Strava actions can create, update, upload, favorite, or otherwise modify user data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Strava skill page](https://clawhub.ai/oomol/skills/oo-strava)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Strava homepage](https://www.strava.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
