## Description:

Trigger.dev helps agents read, create, and update Trigger.dev data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Trigger.dev run state, retrieve run results, replay or cancel runs, and trigger tasks through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing Trigger.dev actions, including canceling, triggering, or replaying runs, can affect live workflows.

Mitigation: Confirm the exact task or run identifier, payload, and intended effect with the user before executing write actions.

Risk: Setup instructions include remote installer pipelines and account connection steps.

Mitigation: Install and connect the oo CLI only from independently trusted and verified sources; avoid running installer pipelines without review.

## Reference(s):

- [Trigger.dev homepage](https://trigger.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trigger-dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, connector schema checks, JSON payload examples, and run-management guidance.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
