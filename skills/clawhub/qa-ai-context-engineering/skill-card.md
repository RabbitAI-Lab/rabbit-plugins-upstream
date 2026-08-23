## Description:

Packages prior QA analysis such as requirements, scenario trees, boundaries, and risks into a structured AI context package for generating higher-quality test cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill after requirements decomposition and scenario design to assemble business, functional, and technical context for downstream AI test-case generation. When upstream analysis is incomplete, it can read provided requirement files or fetch user-supplied URLs to structure supplemental context while marking missing inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requirement documents, private URLs, and internal system details may contain confidential information.

Mitigation: Review inputs before use and avoid providing sensitive material unless the execution environment is approved for that data.

Risk: Fetched URLs can introduce incomplete, stale, or untrusted context into the generated test package.

Mitigation: Use trusted source URLs and validate any extracted assumptions before passing the context to downstream test generation.

## Reference(s):

- [Test Case Output Template](references/output-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown context package]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scenario summaries, boundary lists, risk indicators, and traceability to upstream requirement and scenario IDs.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
