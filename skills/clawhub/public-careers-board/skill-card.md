## Description:

Fetches current public jobs from a selected Acxiom, LiveRamp, or Magnite careers board and reports source coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[epistemedeus](https://clawhub.ai/user/epistemedeus)

### License/Terms of Use:

MIT

## Use Case:

Job seekers and developers use this skill to retrieve public listings from one supported company board and assess whether the returned jobs are complete, partial, empty, or unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill contacts public careers endpoints.

Mitigation: Use the documented command with one supported board and review its source and coverage before relying on results.

Risk: Requesting a local result file creates an additional copy of the observation.

Mitigation: Use --out only when you intend to create a new local file.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/epistemedeus/skills/public-careers-board)
- [Official Ashby public job posting API](https://developers.ashbyhq.com/docs/public-job-posting-api)
- [Magnite careers page](https://www.magnite.com/careers/)
- [Bundled source pins](references/source-pins.json)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON observation with job rows and coverage; text summary for the caller]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional new local result file when explicitly requested with --out.]

## Skill Version(s):

0.1.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
