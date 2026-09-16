## Description:

WebinarJam helps agents use an OOMOL-connected WebinarJam account to list webinars, inspect webinar or registrant details, and register users through the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators with WebinarJam accounts use this skill to retrieve webinar, registrant, and attendee information through an OOMOL-connected account. The skill can also register a user for a webinar after the agent confirms the exact write payload with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes direct execution of remote installer scripts.

Mitigation: Review the oo CLI installation path, prefer official signed or checksum-verified installers, and avoid blindly running curl | bash or irm | iex.

Risk: The register_user action can change WebinarJam data.

Mitigation: Confirm the exact registration payload and intended effect with the user before running the write action.

## Reference(s):

- [ClawHub WebinarJam Skill Page](https://clawhub.ai/oomol/skills/oo-webinarjam)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [WebinarJam Homepage](https://webinarjam.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
