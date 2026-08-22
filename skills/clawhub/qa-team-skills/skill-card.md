## Description:

QA Team Skills helps testing teams route natural-language QA requests into standardized workflows for requirements review, test case design, agent testing, defect analysis, reporting, team management, quality assessment, regression testing, and exploratory testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT

## Use Case:

QA engineers, test managers, and developers use this skill to standardize AI-assisted testing work across requirements review, case generation, agent testing, defect analysis, reports, team dashboards, release checks, and exploratory testing. It is designed to fit existing QA workflows while keeping human review as the decision point.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist sensitive requirements, defect history, reports, or QA memory to local files.

Mitigation: Use sanitized QA inputs, avoid production credentials and customer data, and confirm memory writes deliberately before allowing local persistence.

Risk: The skill can reuse local QA memory, which may carry stale or sensitive historical context into later tasks.

Mitigation: Review loaded memory before relying on it, decline memory loading when working on sensitive material, and clear obsolete module data when it is no longer needed.

Risk: PRD review workflows may create Markdown files in docs/reviews unless export is explicitly disabled.

Mitigation: Tell the agent not to export when review output should remain transient, and inspect generated review files before sharing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-team-skills)
- [README](README.md)
- [User Manual](docs/user-manual.md)
- [Process Integration Guide](docs/process-integration.md)
- [Memory Module](memory/README.md)
- [CI and Quality Validation](docs/ci-testing.md)
- [Changelog](docs/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration, Files]

**Output Format:** [Markdown and structured text, with optional local JSON memory records and Markdown review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are prompt-generated QA artifacts and may include locally persisted memory files or PRD review Markdown exports when the workflow calls for them.]

## Skill Version(s):

v1.6.5 (source: frontmatter, VERSION, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
