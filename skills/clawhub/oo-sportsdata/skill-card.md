## Description:

SportsDataIO connector guidance for reading, creating, and updating SportsDataIO data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SportsDataIO through the OOMOL `oo` CLI, inspect live action schemas, run connector actions, and handle setup or recovery issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Request parameters and payload data are sent through OOMOL to SportsDataIO.

Mitigation: Install only when an OOMOL-connected SportsDataIO account is intended and review payloads before running connector actions.

Risk: Tagged write actions may change SportsDataIO state.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write, and require explicit approval for destructive actions.

## Reference(s):

- [SportsDataIO homepage](https://sportsdata.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sportsdata)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
