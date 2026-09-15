## Description:

Use this skill for Acuity Scheduling requests, including reading, creating, and updating data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Acuity Scheduling through an OOMOL-connected account, including retrieving account data, listing calendars and appointments, checking availability, and creating, updating, rescheduling, or cancelling appointments with confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts directly in the shell.

Mitigation: Review and verify the OOMOL installer source before use, or prefer a pinned, signed, or package-manager installation path for the oo CLI.

Risk: Write actions can create, update, reschedule, or cancel Acuity Scheduling appointments.

Mitigation: Confirm the exact action, target record, payload, and expected effect with the user before running any write action.

## Reference(s):

- [Acuity Scheduling homepage](https://acuityscheduling.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require explicit user confirmation; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
