## Description:

PagerDuty (pagerduty.com). Use this skill for ANY PagerDuty request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, incident response, and support teams use this skill to inspect PagerDuty incidents, list on-call assignments, and make approved incident state changes through an OOMOL-connected PagerDuty account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change PagerDuty incident state, including acknowledgement, update, and resolution actions.

Mitigation: Require explicit user approval for every incident state change, with the target incident and payload confirmed before execution.

Risk: Installing the oo CLI via a remote install script can bypass strict change-control expectations.

Mitigation: Install the CLI through a verified and pinned method when operating in controlled environments.

## Reference(s):

- [PagerDuty homepage](https://www.pagerduty.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pagerduty)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs an agent to inspect live connector schemas before running PagerDuty actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
