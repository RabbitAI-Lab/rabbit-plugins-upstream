## Description:

Checks franchise settlement worksheets for royalty, advertising fund, payable total, total-row, duplicate-franchisee, and blank-field issues, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Business operations users and agents use this skill to review monthly franchise settlement tables where payable totals depend on royalty, minimum guarantee, and advertising fund calculations. It reports deterministic worksheet findings when the input table has the required headers and enough detail to check.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles worksheet text through a local Node script.

Mitigation: Run it only in an environment where local processing of the worksheet text is acceptable, and avoid supplying data beyond the settlement table needed for the check.

Risk: The artifact documentation references a paid-upgrade flow that uses an unpinned external installer and separate purchase steps.

Mitigation: Review the package and source before using the upgrade path, avoid mutable @latest execution when possible, and require explicit human confirmation for wallet authorization or payment.

Risk: The free tier does not run all possible validation checks for franchise settlement data.

Mitigation: Review the reported executed, withheld, and out-of-scope checks before relying on a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/franchise-royalty-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay storefront referenced by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include line numbers, severity labels, summaries, executed checks, withheld checks, and out-of-scope checks.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
