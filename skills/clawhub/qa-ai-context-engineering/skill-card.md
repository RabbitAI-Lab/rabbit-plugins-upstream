## Description:

This skill packages upstream QA analysis, requirement artifacts, and user-provided URL content into a structured AI context package for test-case generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill after requirement decomposition and scenario analysis to assemble business, functional, technical, boundary, and risk context before prompting an AI to generate test cases. When upstream inputs are missing, it can read provided requirement files or fetch provided URLs while flagging gaps that should still be completed upstream.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive requirement documents or private URLs may be read or fetched when supplied by a user.

Mitigation: Use only intended inputs, avoid sensitive internal PRDs or private links unless access is authorized, and confirm this access is acceptable before installation.

Risk: Fetched web content and user-provided documents can contain untrusted or incomplete information.

Mitigation: Treat external content as untrusted, preserve source labels, and review the resulting context before using it to generate test cases.

Risk: Supplementing missing inputs could be mistaken for completing the upstream QA analysis workflow.

Mitigation: Review missing-item flags and complete upstream requirement, scenario, boundary, and risk analysis when those inputs are required.

## Reference(s):

- [Test Case Output Template](references/output-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown context package]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scenario summaries, boundary conditions, risk indicators, source labels, and missing-context guidance.]

## Skill Version(s):

1.6.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
