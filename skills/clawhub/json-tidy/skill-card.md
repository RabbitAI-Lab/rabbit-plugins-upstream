## Description:

Formats, minifies, sorts, and validates JSON while reporting parse errors with line and column context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to tidy, minify, sort, and validate JSON from files or stdin during everyday development and data handling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writing with --out can overwrite an existing file because the runtime script writes immediately while the documentation claims dry-run safeguards.

Mitigation: Prefer stdout or disposable output files, back up important data, and manually review output paths before writing.

Risk: The documented npx install command is unpinned and may resolve a changing CLI version.

Mitigation: Install only after trusting the resolved package version and reviewing the available ClawHub release evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/json-tidy)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from command-line usage, with human-readable validation errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read stdin or a file and can write formatted output to stdout or an output file.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact manifest.json and README.md agree; artifact/SKILL.md says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
