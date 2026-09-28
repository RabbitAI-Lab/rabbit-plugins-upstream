## Description:

Organizes requirements, scenarios, boundaries, and risks into a structured context package for AI-assisted test-case generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and testers use this skill after requirements and scenario analysis to prepare a structured business, functional, and technical context package for test-case generation. It identifies missing inputs and distinguishes supplied facts from assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded requirements may contain customer data, production secrets, or financial records.

Mitigation: Redact or mask sensitive content before providing requirement files.

Risk: User-provided URLs may expose material that was not intended for analysis.

Mitigation: Provide only URLs that the agent is intended to fetch and analyze.

Risk: Missing upstream analysis can produce incomplete or misleading test context.

Mitigation: Label missing inputs and assumptions, and return to the upstream analysis steps to fill gaps.

## Reference(s):

- [Test-case output template](artifact/references/output-template.md)
- [ClawHub skill listing](https://clawhub.ai/kokxi/skills/qa-ai-context-engineering)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured Markdown context package]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Organizes business goals, functional constraints, optional technical history, and test-output requirements; labels assumptions and missing inputs.]

## Skill Version(s):

1.7.7 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
