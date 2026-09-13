## Description:

Convert and format dates/times with zero external APIs -- ISO 8601, Unix epoch, RFC 2822, and timezone conversion using only the local date binary and TZ database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate local shell recipes for timestamp formatting, epoch conversion, timezone conversion, duration arithmetic, and cron date checks without external APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell examples may behave differently on systems without GNU coreutils date, especially macOS default date.

Mitigation: Review commands before running them and use GNU coreutils gdate on non-GNU date systems.

Risk: Date parsing and timezone results depend on the local TZ database and date implementation.

Mitigation: Confirm critical conversions with a round-trip check and ensure the target system has current zoneinfo data.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs assume GNU coreutils date and a local TZ database; macOS users may need gdate from coreutils.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
