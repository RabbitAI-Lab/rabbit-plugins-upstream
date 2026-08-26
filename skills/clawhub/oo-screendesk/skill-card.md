## Description:

Screendesk lets agents operate Screendesk through an OOMOL-connected account for reading recordings, transcripts, workspace users, and guarded updates to recording metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Screendesk recordings and transcripts, list visible recordings, look up workspace users when authorized, and update recording title, summary, or description after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The update_recording action can change a Screendesk recording's title, summary, or description.

Mitigation: Confirm the exact update_recording payload and expected effect with the user before execution.

Risk: Workspace user listing and search actions may expose user data and require admin credentials.

Mitigation: Run list_users or search_user only for authorized admin workflows and limit requests to the needed lookup.

Risk: The skill depends on the OOMOL oo CLI and an active Screendesk connector.

Mitigation: Install and connect the oo CLI only when the user intends to use this connector, and follow setup steps only after a relevant command fails.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-screendesk)
- [Screendesk Homepage](https://screendesk.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Screendesk Icon](https://static.oomol.com/logo/third-party/screendesk.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before running connector actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
