## Description:

qa-team-skills helps QA teams route natural-language testing requests into standardized workflows for requirements review, test-case design, agent testing, bug analysis, report generation, team management, regression testing, and exploratory testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT

## Use Case:

QA engineers, test managers, and developers use this skill to turn natural-language testing requests into repeatable QA workflows, including PRD review, test-case generation, agent testing, defect analysis, reporting, and team quality summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PRD review workflows can automatically export full review reports into docs/reviews, which may persist sensitive product details in the project workspace.

Mitigation: Redact sensitive inputs before use, explicitly request chat-only output when export is not wanted, and review generated docs/reviews files before sharing or committing.

Risk: The skill can store local testing memory, including test cases, defects, reports, and standards that may contain customer, credential, payment, or screenshot data if supplied by the user.

Mitigation: Avoid providing production secrets or unredacted customer data, confirm memory writes intentionally, and periodically review retained local memory for sensitive content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-team-skills)
- [README](README.md)
- [User manual](docs/user-manual.md)
- [Process integration guide](docs/process-integration.md)
- [CI and quality validation](docs/ci-testing.md)
- [Memory module](memory/README.md)
- [skills.sh listing](https://skills.sh/Kokxi/qa-team-skills)

## Skill Output:

**Output Type(s):** [text, markdown, json, configuration, guidance]

**Output Format:** [Markdown reports, structured tables, JSON memory records, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local QA memory and export Markdown PRD review reports when the selected workflow calls for it.]

## Skill Version(s):

1.6.4 (source: evidence.release.version, artifact/VERSION, artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
