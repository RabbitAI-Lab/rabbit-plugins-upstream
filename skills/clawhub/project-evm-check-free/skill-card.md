## Description:

Checks project earned value management worksheets for CV, SV, CPI, SPI, total-row, duplicate, and blank-field issues, with each finding tied to source line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Project managers, cost controllers, and engineering teams use this skill to validate copied or JSON-formatted EVM tables before reporting project progress and cost performance. It focuses on deterministic arithmetic checks and flags missing data rather than making project-management judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed checker appears local, but the documentation and normal output direct users toward unpinned external installation and a paid SkillPay purchase flow.

Mitigation: Use the bundled free checker without following the upgrade prompt unless the publisher, package source, and payment flow have been independently verified and the user explicitly intends to install external payment tooling.

Risk: The free artifact intentionally withholds several EVM checks and may omit issues covered only by a separate paid skill.

Mitigation: Treat the output as limited to the listed free checks and review withheld or out-of-scope EVM conditions separately before relying on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/project-evm-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact SKILL.md](artifact/SKILL.md)
- [Sample input JSON](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with local shell commands and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; findings cite input line numbers; insufficient input returns missing-field guidance instead of a conclusion.]

## Skill Version(s):

1.0.9 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
