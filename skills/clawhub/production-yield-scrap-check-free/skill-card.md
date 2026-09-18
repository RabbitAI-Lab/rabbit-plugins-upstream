## Description:

A local Chinese-language checker for production yield and scrap tables that recalculates row arithmetic, totals, duplicate rows, blanks, and negative quantities, with source-backed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and manufacturing operations users can use this skill during month-end close, reconciliation, or inventory checks to verify production input, output, scrap, and work-in-process table consistency. It is intended for local checks on user-supplied table text and reports insufficient input rather than fabricating conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation and normal human-readable output direct users toward an unpinned remote install and paid purchase workflow outside the local checker.

Mitigation: Treat paid-upgrade instructions as optional; independently verify the package, source, version, and SkillPay workflow before running remote install commands or authorizing payment.

Risk: The free checker omits listed checks, so a clean result is not a complete production-yield or scrap-rate audit.

Mitigation: Review `scope.checks_not_run` and the out-of-scope list before relying on results for operational or financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/production-yield-scrap-check-free)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Paid upgrade purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON results from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include line references, executed checks, checks not run, summary counts, and insufficient-input status when required table fields are missing.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
