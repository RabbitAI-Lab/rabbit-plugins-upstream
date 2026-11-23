## Description:

Read Speediance workouts and exercise data, and create custom training programs for a Gym Monster machine, with optional calendar reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stozo04](https://clawhub.ai/user/stozo04)

### License/Terms of Use:

MIT-0

## Use Case:

Gym Monster owners and their agents can review completed workouts, look up exercises, and prepare training programs. The skill can also reserve a program on the machine calendar when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses account credentials and a live session token; config.json stores the password in plaintext.

Mitigation: Prefer environment variables or a secret store, avoid sharing config.json, and protect credential and token files.

Risk: Pushing a program or reserving a date changes the user's Speediance account.

Mitigation: Review the plan with `--dry-run` first and make account changes only when the user requests them.

Risk: Gym Monster 2 behavior is untested and exercise IDs can differ by device.

Mitigation: Use the documented Gym Monster v1 setting where possible and check exercise resolution before pushing a plan.

## Reference(s):

- [Speediance CLI source repository](https://github.com/stozo04/speediance-cli)
- [Speediance CLI releases](https://github.com/stozo04/speediance-cli/releases)

## Skill Output:

**Output Type(s):** [JSON data, Shell commands, Configuration guidance]

**Output Format:** [Structured JSON for CLI results, with concise setup and usage guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workout fields are returned as supplied by the service; JSON output is available for parsing.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
