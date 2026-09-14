## Description:

Locates, verifies, optionally downloads, and extracts official China CDC surveillance reports for influenza, acute respiratory infections, COVID-19, and infectious-disease risk assessments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find official China CDC surveillance reports, verify their source URLs, download PDFs when requested, and extract report metadata or content for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run bundled Python scripts and write report artifacts locally.

Mitigation: Install and run it only in environments where local artifact writes are acceptable, and review generated files before reuse.

Risk: PDF extraction depends on installing a Python package at runtime.

Mitigation: Use an isolated environment and pin or hash dependencies before running the install step.

Risk: Extracted public-health report content could be mistaken for medical advice or prediction.

Mitigation: Use outputs for locating and extracting official report content only, not for diagnosis, treatment, prediction, or clinical guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/miaoshou.dev/skills/cdc-data)
- [China CDC official site](https://www.chinacdc.cn/)
- [Source registry](references/source-registry.md)
- [Workflow](references/workflow.md)
- [Matching rules](references/matching-rules.md)
- [Output schema](references/output-schema.md)
- [PDF extraction rules](references/pdf-extraction-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Concise text or Markdown with verified URLs, status fields, saved paths, and optional JSON extraction artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local report artifacts or verified PDF downloads only when requested]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
