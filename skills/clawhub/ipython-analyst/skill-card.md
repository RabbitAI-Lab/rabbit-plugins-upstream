## Description:

Run Python interactively to analyze data, debug code, profile performance, validate schemas, process large files, inspect ASTs, and produce diagnostic outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[darkd](https://clawhub.ai/user/darkd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and engineers use this skill to investigate Python, data, schema, profiling, parsing, and code-analysis problems through interactive execution. It is intended for diagnostic work that returns fixes, reports, validation results, generated files, or concise guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Interactive Python execution can run unsafe uploaded code or inspect sensitive local files.

Mitigation: Review untrusted code before execution, keep work scoped to the documented upload and download paths, and use the bundled safe-execution utilities where appropriate.

Risk: Tracebacks, logs, saved repro inputs, or baselines may contain secrets or sensitive debugging data.

Mitigation: Avoid printing unnecessary traceback locals, redact sensitive values in reports, and clean up saved repro inputs or baselines that contain sensitive data.

Risk: Regex, parser, or large-data tasks can hang or exhaust memory.

Mitigation: Wrap unbounded work in timeout_context and use chunked or Dask processing for large files instead of loading everything into memory.

## Reference(s):

- [Code Analysis Reference](references/code-analysis.md)
- [Data Analysis Reference](references/data-analysis.md)
- [Debugging Reference](references/debugging.md)
- [Distributed Processing Reference](references/distributed.md)
- [Environment & Session Reference](references/environment.md)
- [Machine Learning Reference](references/machine-learning.md)
- [Network Analysis Reference](references/network-analysis.md)
- [Schema Validation Reference](references/schema-validation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown responses with Python code snippets and optional generated files such as CSV, JSON, PNG, SVG, DOT, or joblib outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes generated artifacts to /home/z/my-project/download/ when files are needed.]

## Skill Version(s):

7.0.0 (source: server release evidence and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
