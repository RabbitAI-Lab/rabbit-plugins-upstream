## Description:

Checks safety production fee extraction and use tables by recalculating row amounts and totals, detecting duplicates, blanks, and negative values, and citing source lines for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, especially safety management and finance teams, use this skill around monthly closing and safety-fee accounting workflows to check safety production fee extraction and use tables. It helps recalculate declared amounts, verify balance roll-forward and totals, and flag duplicate, blank, placeholder, or negative entries without making legal or accounting judgments outside the supplied table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an optional paid upgrade workflow that asks an agent to install and run unpinned remote code.

Mitigation: Use the free local checker only, or separately verify the package, exact version, source, payment flow, and newly installed instructions in a controlled environment before running the paid workflow.

Risk: The checker intentionally omits several complete-edition checks, so its output is limited to the free local checks.

Mitigation: Treat results as table-level arithmetic and completeness checks only, and review the listed withheld and out-of-scope checks before relying on the output for compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/safety-production-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Upgrade purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs a local Node.js checker; insufficient input returns missing-field guidance rather than a positive or negative conclusion.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
