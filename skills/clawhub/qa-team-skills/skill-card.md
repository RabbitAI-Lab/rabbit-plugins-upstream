## Description:

QA Team Skills provides a unified prompt workflow for QA teams to turn natural-language testing requests into requirements reviews, test cases, agent test plans, bug analysis, reports, team management summaries, exploratory testing guidance, and local memory-supported reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT

## Use Case:

QA engineers, test managers, and software teams use this skill to standardize AI-assisted testing work across requirements review, test design, defect analysis, reporting, team quality management, and exploratory testing while keeping human review in the loop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep QA artifacts such as test cases, defect analyses, reports, and team summaries in local memory files.

Mitigation: Install only when local retention is acceptable, avoid credentials, customer PII, sensitive screenshots, and production identifiers unless approved, and require confirmation before loading historical memory or writing or deleting files.

Risk: Historical memory may influence new QA outputs if loaded into the current task context.

Mitigation: Ask before loading historical memory and let users decline memory use for sensitive or one-off tasks.

Risk: Generated QA recommendations, root-cause analysis, and management summaries may be incomplete or misleading if used without review.

Mitigation: Review high-priority cases, low-confidence root-cause analysis, management reports, and release decisions against source systems and human tester judgment before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-team-skills)
- [README](README.md)
- [User manual](docs/user-manual.md)
- [Process integration guide](docs/process-integration.md)
- [Memory module documentation](memory/README.md)
- [CI and quality validation](docs/ci-testing.md)
- [skills.sh listing](https://skills.sh/Kokxi/qa-team-skills)

## Skill Output:

**Output Type(s):** [text, markdown, json, configuration, guidance]

**Output Format:** [Markdown responses with structured tables, checklists, and optional JSON memory records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include QA artifacts such as test cases, defect analyses, reports, team summaries, exploratory notes, and prompts to confirm local memory operations.]

## Skill Version(s):

v1.6.1 (source: server release metadata, SKILL.md frontmatter, VERSION, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
