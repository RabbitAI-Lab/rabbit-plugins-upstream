## Description:

Convert any time representation - unix timestamps (s/ms/us/ns), ISO 8601/RFC 3339/RFC 2822, strftime, spreadsheet serials, IANA timezones, natural language ("3 days ago"/"下周一"), date arithmetic, durations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzzqiuchan](https://clawhub.ai/user/zzzqiuchan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert timestamps, date strings, natural-language dates, timezones, date arithmetic, and durations with a bundled local Python helper instead of doing error-prone time math by hand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Timezone-sensitive answers can be wrong if naive input is interpreted in the wrong source timezone or if ambiguity notes are ignored.

Mitigation: Review the displayed timezone, pass --in-tz explicitly when the source timezone is known, and surface ambiguity notes before relying on the result.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Plain text or Markdown with shell commands; the helper can emit JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include timezone context and ambiguity notes when they affect the answer.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
