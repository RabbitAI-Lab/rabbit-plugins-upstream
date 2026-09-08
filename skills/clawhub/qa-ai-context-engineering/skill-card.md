## Description:

Builds a structured QA context package from requirement analysis, scenario trees, boundary lists, risk signals, and related inputs so an agent can generate better test cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill after requirement and scenario analysis to package business, functional, technical, boundary, and risk context before prompting an AI to generate test cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read requirement documents or fetch user-provided URLs while building QA context.

Mitigation: Use only documents and links that are appropriate for the active agent environment.

Risk: Incomplete upstream analysis can produce an incomplete context package and lower-quality generated test cases.

Mitigation: Mark missing inputs explicitly and return to upstream requirement, scenario, boundary, combination, state, or risk analysis before final prompt generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-ai-context-engineering)
- [Output template](references/output-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured QA context sections and test case tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes context package, scenario summary, boundary list, risk indicators, traceability guidance, priority distribution, and coverage notes.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter is 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
