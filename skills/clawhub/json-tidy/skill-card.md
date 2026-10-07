## Description:

Formats, minifies, validates, and optionally sorts JSON keys, with line-and-column feedback for parse errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theoretical text all rights reserved

## Use Case:

Developers and other users can format or validate local JSON files and piped JSON, producing readable or compact output and locating syntax errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using --out writes immediately and can overwrite an existing file despite documentation describing a dry-run and --apply workflow.

Mitigation: Choose output paths carefully and back up important files before using --out.

Risk: Documentation mentions --json and --apply options that the script does not support.

Mitigation: Check the script's --help output for supported options before relying on documented commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/json-tidy)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [JSON, Text, Files]

**Output Format:** [Pretty-printed or minified JSON on stdout or in a file; plain-text parse errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional key sorting; UTF-8 file output]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
