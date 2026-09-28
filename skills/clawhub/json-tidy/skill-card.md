## Description:

Formats, minifies, sorts, and validates JSON from a file or standard input, reporting the line and column of parsing errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agents use this utility to make JSON readable or compact, sort object keys, and locate parsing errors in local JSON inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation describes dry-run, --apply, and --json options that the utility does not implement.

Mitigation: Check the script's --help output before use; use --out only when a file write is intended.

Risk: Writing to an output path may replace existing file contents.

Mitigation: Review the --out path and back up important files before writing.

## Reference(s):

- [ClawHub json-tidy release](https://clawhub.ai/zhaoxinghua09-cell/skills/json-tidy)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Formatted or minified JSON on standard output or in a file; text for parsing errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional key sorting; parsing errors include line and column.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact versions differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
