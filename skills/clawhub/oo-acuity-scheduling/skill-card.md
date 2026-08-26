## Description:

Use this skill for Acuity Scheduling requests to read, create, cancel, reschedule, and update scheduling data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Acuity Scheduling through OOMOL, including account lookup, appointment retrieval, availability queries, and appointment changes. It is intended for live scheduling workflows where write actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create, cancel, reschedule, or update Acuity Scheduling appointments and related client details.

Mitigation: Confirm the exact payload and expected effect with the user before running write or destructive actions.

Risk: Payloads may be incorrect if the connector contract changes.

Mitigation: Inspect the live action schema before constructing or running each connector request.

Risk: The skill can read scheduling data through the connected OOMOL account.

Mitigation: Install and use it only when Acuity Scheduling access through OOMOL is intended.

## Reference(s):

- [Acuity Scheduling homepage](https://acuityscheduling.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Acuity Scheduling skill on ClawHub](https://clawhub.ai/oomol/skills/oo-acuity-scheduling)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects with data and meta execution details.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
