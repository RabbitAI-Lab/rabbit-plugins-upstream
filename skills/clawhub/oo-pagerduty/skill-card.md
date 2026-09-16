## Description:

PagerDuty (pagerduty.com). Use this skill for ANY PagerDuty request - reading, creating, and updating data. Whenever a task involves PagerDuty, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and incident responders use this skill to inspect PagerDuty incidents, on-call assignments, and current-user context, and to perform confirmed incident updates through an OOMOL-connected PagerDuty account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident state-changing actions may acknowledge, resolve, or update PagerDuty incidents without sufficient confirmation.

Mitigation: Require explicit confirmation of the exact incident ID, acting user, payload, and intended new state before executing any acknowledge, resolve, or update action.

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts directly into a shell or PowerShell.

Mitigation: Avoid direct remote-script execution unless the installer source is independently trusted and verified; prefer a reviewed manual installation path where available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pagerduty)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [PagerDuty Homepage](https://www.pagerduty.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke OOMOL oo CLI connector actions that return JSON responses from PagerDuty]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
