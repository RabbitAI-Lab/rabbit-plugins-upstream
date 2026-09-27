## Description:

yotta-item deterministically assembles exam papers from a local item bank and blueprint, and checks existing papers for coverage, score, difficulty, section, and time gaps without network or model calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, curriculum teams, and developers use this skill to assemble reproducible exam papers from local item banks and to automate deterministic paper checks in batch jobs or CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can overwrite an existing yotta-item folder in an agent skill directory.

Mitigation: Install from a trusted or pinned source, prefer --agent or --dir to target a known directory, and back up any existing yotta-item folder before reinstalling.

Risk: Exam assembly and checking depend on the quality and completeness of the local item bank and blueprint.

Mitigation: Validate the bank and blueprint first, review any reported gaps, and keep final paper approval with the responsible educators.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-item)
- [Project Homepage](https://github.com/YottaMeta/yotta-item)
- [Bank Format](references/bank-format.md)
- [Blueprint Format](references/blueprint-format.md)
- [Report Format](references/report-format.md)
- [Privacy and Boundaries](references/privacy.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports and JSON artifacts produced through local CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic for fixed inputs and seed; local-only with no network or model calls.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
