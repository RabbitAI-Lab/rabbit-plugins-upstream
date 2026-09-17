## Description:

Use this skill for Acuity Scheduling requests, including reading, creating, and updating scheduling data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Acuity Scheduling through an OOMOL-connected account. It supports retrieving account, appointment, calendar, appointment type, intake form, and availability data, and creating, updating, rescheduling, or canceling appointments after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends remote shell and PowerShell installers that should not be run blindly.

Mitigation: Use a verified official installer or package source where possible before installing the oo CLI.

Risk: Scheduling data is routed through OOMOL and uses an OOMOL-connected credential for reads and writes.

Mitigation: Confirm that this data routing and credential use are acceptable before installation and use.

Risk: Create, cancel, reschedule, and update actions can change Acuity Scheduling state.

Mitigation: Confirm the exact action payload and expected effect with the user before executing any write action.

## Reference(s):

- [ClawHub Acuity Scheduling Skill](https://clawhub.ai/oomol/skills/oo-acuity-scheduling)
- [Acuity Scheduling](https://acuityscheduling.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
