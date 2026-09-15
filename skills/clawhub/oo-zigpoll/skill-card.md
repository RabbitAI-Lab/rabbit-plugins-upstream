## Description:

Operate Zigpoll through an OOMOL-connected account by inspecting live connector schemas and running Zigpoll connector actions with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to retrieve Zigpoll user, account, poll, slide, participant, and response data, and to generate unique survey links through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer one-liners that execute shell or PowerShell scripts.

Mitigation: Prefer a verified package manager, pinned release, checksum validation, or manual installer inspection before running setup commands.

Risk: Connector actions can read Zigpoll account, participant, and response data available to the connected OOMOL account.

Mitigation: Limit requests to the needed account, poll, or slide, and avoid returning unnecessary participant or response data.

Risk: Generated survey links are unique and trackable.

Mitigation: Confirm the poll target and intended use before generating or sharing survey links.

## Reference(s):

- [ClawHub Zigpoll skill](https://clawhub.ai/oomol/skills/oo-zigpoll)
- [Zigpoll homepage](https://www.zigpoll.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses can include Zigpoll account, participant, poll, slide, response, and generated survey-link data available to the connected OOMOL account.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
