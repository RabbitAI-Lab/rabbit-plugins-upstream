## Description:

QA Team Skills gives test teams a standardized AI-assisted workflow for requirement review, test-case design, AI agent testing, bug analysis, reporting, team management, exploratory testing, and reusable local QA memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT

## Use Case:

QA engineers, test managers, and development teams use this skill to turn product requirements, defects, test scope, and team status into structured QA artifacts such as review findings, test cases, bug analyses, reports, and management summaries. It is intended to standardize team prompts and preserve reusable QA memory across iterations while leaving final testing decisions to humans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad natural-language routing plus local memory can read and retain sensitive QA data across later chats.

Mitigation: Use explicit /qa commands where possible, avoid unrelated generic trigger phrases, and review or disable memory behavior when strict per-project isolation is required.

Risk: QA memory may retain production credentials, personal data, real payment identifiers, screenshots, or sensitive logs if users provide them.

Mitigation: Do not paste sensitive or unredacted production data unless local retention and model-session use are approved by the organization.

Risk: Generated QA analyses and reports can be incomplete or misleading if treated as final testing decisions.

Mitigation: Require human review for high-severity findings, P0 test cases, lower-confidence root-cause analysis, and management-facing reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-team-skills)
- [User manual](docs/user-manual.md)
- [Process integration guide](docs/process-integration.md)
- [Memory module](memory/README.md)
- [CI and quality validation](docs/ci-testing.md)
- [Changelog](docs/CHANGELOG.md)
- [skills.sh listing](https://skills.sh/Kokxi/qa-team-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown reports, tables, checklists, and structured JSON memory records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference locally retained QA memory under memory/data/products when the skill is used in workflows that enable memory.]

## Skill Version(s):

v1.6.0 (source: frontmatter, VERSION, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
