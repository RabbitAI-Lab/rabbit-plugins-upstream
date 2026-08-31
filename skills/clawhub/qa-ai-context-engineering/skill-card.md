## Description:

Packages requirements decomposition, scenario trees, boundary lists, risk notes, and related QA analysis into a structured AI context package for generating higher-quality test cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test architects, and development teams use this skill after requirements and scenario analysis to assemble a structured context package for downstream AI test-case generation. It can also parse user-provided requirement files or user-pasted URLs when upstream analysis is incomplete, while marking missing inputs for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read user-supplied requirement files or fetch URLs pasted by the user, which can expose confidential documents or internal resources if provided unintentionally.

Mitigation: Provide only documents and URLs intended for the QA context-building task, and avoid confidential files or internal/private URLs unless their use is deliberate.

Risk: Incomplete upstream requirement, scenario, boundary, or risk analysis can lead to gaps in the generated context package and lower-quality downstream test cases.

Mitigation: Review missing-input annotations and return to the relevant upstream analysis steps before relying on the context for final test-case generation.

## Reference(s):

- [Output Template](references/output-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown context package]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes business context, functional boundaries, optional technical and historical-defect notes, output-quality requirements, missing-input annotations, and traceability guidance.]

## Skill Version(s):

1.7.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
