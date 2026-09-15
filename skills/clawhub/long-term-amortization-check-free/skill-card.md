## Description:

Checks Chinese long-term prepaid expense amortization ledgers locally for arithmetic, totals, duplicate items, and missing fields, with findings citing source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or inventory checks to verify long-term prepaid expense amortization ledgers before continuing downstream accounting work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional paid-upgrade instructions ask an agent to run a mutable remote installer and follow newly installed purchase instructions.

Mitigation: Review the official SkillPay instructions and package provenance before installation; require explicit confirmation before any install, wallet authorization, or purchase step.

Risk: The free checker omits several validation checks that are described as part of a separate full version.

Mitigation: Treat results as coverage-limited and review the listed checks not run and out-of-scope items before relying on the output.

Risk: Ledger data may contain sensitive financial information.

Mitigation: Use only ledger text appropriate for local processing; the artifact states the checker runs locally and does not use the network.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/long-term-amortization-check-free)
- [SkillPay full-version shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay upgrade installation guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs a local Node.js checker against ledger table text or JSON input; the artifact states no network use.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
