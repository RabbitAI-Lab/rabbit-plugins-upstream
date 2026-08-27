## Description:

Routes QA requests to specialized workflows for PRD review, test-case design, AI agent testing, bug analysis, reporting, team management, and exploratory testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT

## Use Case:

QA engineers and test managers use this skill to triage natural-language QA requests and generate structured reviews, test cases, agent test plans, bug analysis, reports, team summaries, and exploratory testing outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist local QA history and export PRD review files into a project.

Mitigation: Confirm file-writing actions, review generated files before committing or sharing, and avoid entering secrets, production credentials, customer personal data, or sensitive screenshots.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-team-skills)
- [Publisher profile](https://clawhub.ai/user/kokxi)
- [Unified QA routing prompt](references/qa/prompt.md)
- [QA validation rules](references/qa/validation-rules.md)
- [Human guidance](references/HUMAN-GUIDANCE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Files]

**Output Format:** [Markdown reports and structured JSON records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain local QA history under memory/data/products/{module} after confirmation and may export PRD review Markdown under docs/reviews.]

## Skill Version(s):

1.7.0 (source: ClawHub release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
