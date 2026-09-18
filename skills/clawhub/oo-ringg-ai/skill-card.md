## Description:

Ringg AI (ringg.ai) helps agents operate Ringg AI through OOMOL for reading data and running supported actions instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Ringg AI through an OOMOL-connected account, including reading assistants, calls, workspace details, voices, and caller numbers. It can also initiate outbound calls after the user confirms the destination, caller number, assistant, payload, and possible cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate outbound Ringg AI calls, which may change account state and incur cost.

Mitigation: Require explicit confirmation of the destination, caller number, assistant, payload, and possible cost before running initiate_call.

Risk: The documented first-time setup includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Use those installers only after independently trusting and verifying the OOMOL CLI installer source.

## Reference(s):

- [Ringg AI homepage](https://www.ringg.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Ringg AI skill page](https://clawhub.ai/oomol/skills/oo-ringg-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Ringg AI action data as JSON through the OOMOL oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
