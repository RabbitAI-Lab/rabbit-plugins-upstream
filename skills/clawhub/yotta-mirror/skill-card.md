## Description:

Turns structured class scores and question-to-knowledge mappings into reproducible learning-diagnostics reports with traceable evidence and review flags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education teams use this skill to examine class assessments, identify weak knowledge areas and borderline results, and review evidence before planning instruction. Developers can use its structured reports and exit codes in local automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reproducible student identifier hashes are not sufficient anonymization for externally shared reports.

Mitigation: Use stronger local redaction or keyed/random aliases before sharing, and follow school data-handling rules.

Risk: Installer operations can persistently modify agent skill directories.

Mitigation: Install only to the intended agent or directory, preferably from a pinned package version or reviewed source checkout.

Risk: Small samples or borderline results can be misleading if treated as conclusive student evaluations.

Mitigation: Keep low-sample and borderline findings for teacher review; do not use reports for rankings or consequential student decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-mirror)
- [Project homepage (declared in skill metadata; not verified import provenance)](https://github.com/YottaMeta/yotta-mirror)
- [Input data format](references/data-format.md)
- [Report format](references/report-format.md)
- [Privacy guidance](references/privacy.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Configuration]

**Output Format:** [Markdown or JSON diagnostic report; CSV and JSON input templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include item-level evidence, thresholds and human-review flags; optional exit-code gate for automation.]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
