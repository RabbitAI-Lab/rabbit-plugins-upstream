## Description:

Use this skill for Acuity Scheduling requests that read, create, update, reschedule, cancel, or inspect scheduling data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Acuity Scheduling from an agent, including appointment lookup, availability checks, appointment creation, rescheduling, updates, and cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, reschedule, or cancel appointments using the connected Acuity Scheduling account.

Mitigation: Require the user to confirm the exact payload and effect before write actions, and require explicit approval before cancellation.

Risk: First-time setup includes remote installer one-liners for the oo CLI.

Mitigation: Prefer reviewed or manual installation steps before running remote installer commands.

Risk: The skill depends on OOMOL-managed credentials and connector execution.

Mitigation: Install only when the user trusts OOMOL and is comfortable with the agent using the connected Acuity Scheduling account.

## Reference(s):

- [Acuity Scheduling homepage](https://acuityscheduling.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-acuity-scheduling)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
