## Description:

Fetches public Acxiom or LiveRamp job listings with their source and coverage status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[epistemedeus](https://clawhub.ai/user/epistemedeus)

### License/Terms of Use:

MIT

## Use Case:

Job seekers and research teams use this skill to retrieve public listings from a selected Acxiom or LiveRamp careers board and assess whether the returned coverage is complete, partial, empty, or unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A public board may be unreachable or return incomplete listings.

Mitigation: Check the coverage status before treating results as complete or an empty board.

Risk: The optional --out argument writes a result file.

Mitigation: Review the destination path before running the command.

Risk: The bundled recipe's standalone command reads more than the selected board.

Mitigation: Use the documented scripts/cli.mjs entrypoint unless broader behavior is intentional.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/epistemedeus/skills/public-careers-board)
- [Public careers board recipe](https://agents.samedaydesk.com/recipes/careers-board-cold)
- [Ashby public job posting API](https://developers.ashbyhq.com/docs/public-job-posting-api)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Single-line JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes job rows, source and coverage classification; optional --out writes the result to a new file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
