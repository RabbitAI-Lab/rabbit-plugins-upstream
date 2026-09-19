## Description:

Swiss-army knife for JSON files. Pretty-print, validate, minify, sort keys, and query with dot-notation paths. Zero dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claudiodrusus](https://clawhub.ai/user/claudiodrusus)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to validate, format, minify, sort, and query JSON files or stdin data during local development and command-line workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input JSON may contain secrets or private API responses that are printed to stdout or written to an output file.

Mitigation: Review sensitive data before passing it through stdin, curl pipelines, or file output options.

Risk: Incorrect query paths can select the wrong JSON value or fail during nested object and array traversal.

Mitigation: Validate query paths against expected JSON structure before using extracted values in downstream workflows.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May print selected JSON content to stdout or write formatted JSON to an output file when requested.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
