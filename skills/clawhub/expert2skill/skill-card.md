## Description:

Expert2Skill guides domain experts through structured interviews to turn tacit evaluation methods into rule_library JSON and local runnable skill packages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external experts use this skill to decide whether an expert method can be rule-based, interview the expert, produce a validated rule_library JSON file, and package a local skill with scripts and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated evaluator scripts and skill packages can encode incorrect or misleading expert rules if the interview output is wrong.

Mitigation: Review generated rule libraries and skill packages before deployment or publication, and run the built-in upload-readiness checks.

Risk: Health, investment, legal, engineering, or similar domains can be mistaken for professional advice.

Mitigation: Keep the generated domain disclaimers, require expert review for open-ended judgments, and avoid presenting results as a substitute for licensed professional advice.

Risk: Upload-readiness checks can inspect local files when pointed at a broad directory.

Mitigation: Run checks only against the intended generated skill package directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/expert2skill)
- [Interview guide](references/interview-guide.md)
- [Rule library schema v2](references/rule-library-schema-v2.md)
- [Sample nutrition rule library](references/sample-nutrition.json)
- [Sample value investor rule library](references/sample-value-investor.json)
- [Stock materials reference](references/stock-materials-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON rule libraries, generated skill files, and Python shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated packages are local-first and may include Python evaluator scripts, package metadata, and upload-readiness checks.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
