## Description:

Formats, minifies, and validates JSON from local files or stdin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to pretty-print, compact, or validate JSON payloads from stdin or local files during debugging, configuration review, and data preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: JSON read from a local file or stdin can be printed to stdout, which may expose sensitive content in terminals, logs, or redirected output.

Mitigation: Use the skill only on JSON whose contents are appropriate to display or store in the chosen output destination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/json-formatter)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown with inline bash commands and JSON or plain-text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads from stdin or a local file path; the format action supports configurable indentation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
