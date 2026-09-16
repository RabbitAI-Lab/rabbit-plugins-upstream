## Description:

Checks hotel OTA commission and net settlement tables by recalculating commissions, net settlements, totals, duplicate channels, and blank placeholders, with source line citations for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Hotel and homestay operators use this skill to check monthly OTA settlement statements from channels such as Ctrip, Meituan, and Fliggy. It helps recalculate commissions, net settlement amounts, column totals, duplicate channel rows, and missing values before financial reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker steers users toward an external paid-install and purchase flow using an unpinned @latest package.

Mitigation: Do not run the paid-install command unless the user explicitly wants that separate purchase flow and has independently verified the external package and source.

Risk: The free version omits several checks, including rate-range, negative settlement, negative fee, and high total deduction checks.

Mitigation: Treat passing output as limited to the checks listed as executed, and review omitted checks separately when they matter for settlement decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ota-commission-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown-style guidance and command output; optional JSON result output from the local checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines when checks run; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.10 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
