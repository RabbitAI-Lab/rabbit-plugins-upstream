## Description:

Run Python interactively to analyze data, debug code, profile performance, validate schemas, process large files, and inspect ASTs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[darkd](https://clawhub.ai/user/darkd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data practitioners, and technical agents use this skill for hands-on Python investigation, including data analysis, debugging, profiling, schema validation, static code inspection, and large-file processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to run Python over uploaded files and create output artifacts.

Mitigation: Install it only for workflows that require interactive Python analysis, provide only files approved for that environment, and review generated artifacts before sharing.

Risk: Running untrusted code or inspecting exception locals can expose secrets or trigger unsafe behavior.

Mitigation: Avoid executing untrusted code, redact sensitive inputs when possible, and inspect locals only when necessary for debugging.

Risk: Adding arbitrary paths to the Python import path could cause unintended code execution.

Mitigation: Import only skill-owned helper modules and do not add untrusted paths to sys.path.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/darkd/skills/ipython-analyst)
- [Code Analysis Reference](references/code-analysis.md)
- [Data Analysis Reference](references/data-analysis.md)
- [Debugging Reference](references/debugging.md)
- [Distributed Processing Reference](references/distributed.md)
- [Environment & Session Reference](references/environment.md)
- [Machine Learning Reference](references/machine-learning.md)
- [Network Analysis Reference](references/network-analysis.md)
- [Schema Validation Reference](references/schema-validation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses with inline Python or shell snippets and generated analysis files such as CSV, JSON, PNG, SVG, or reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts should be saved to the user-downloadable output directory and summarized rather than dumped verbatim when large.]

## Skill Version(s):

7.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
