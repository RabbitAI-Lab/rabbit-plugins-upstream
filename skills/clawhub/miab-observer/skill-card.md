## Description:

Observe the MIAB transaction ledger: render callback events to a human-readable log, and optionally post closed-bottle summaries to a chat target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albzhu](https://clawhub.ai/user/albzhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to monitor an MIAB broker ledger, produce readable local transaction logs, and optionally send closed-bottle summaries to a configured chat target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A misconfigured chat target could send closed-bottle summaries to the wrong destination.

Mitigation: Review CLAW_CLOSED_TARGET carefully and use the dry-run command before enabling delivery.

Risk: Reset or damaged notifier state can cause previously closed bottles to be posted again.

Mitigation: Protect the state files and repair cursor state deliberately rather than resetting it casually.

Risk: The observer requires miab-broker 2.0.0 or later and will not produce useful ledger output without an initialized broker state directory.

Mitigation: Install and initialize miab-broker 2.0.0 or later before enabling observer sweeps or notification jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/albzhu/skills/miab-observer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local log entries and optional chat notification summaries; dry-run mode can preview notification content without sending.]

## Skill Version(s):

2.0.0 (source: server release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
