## Description:

Checks copied cash-flow forecast variance tables for net-flow arithmetic, variance arithmetic, total-row consistency, duplicate rows, blank placeholders, and negative flow amounts, with source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill before monthly treasury meetings or rolling forecast reviews to check whether forecast-versus-actual cash-flow tables are internally consistent. It helps identify arithmetic, total-row, duplicate-row, blank-field, and negative-flow issues without assessing business explanations or forecasting quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional upgrade path asks an agent to run an unpinned external installer and follow external purchase or onboarding instructions.

Mitigation: Do not run the external installer or purchase flow unless the package, instructions, and payment step are independently reviewed; prefer a pinned reviewed package version and explicit user approval for each install or purchase action.

Risk: The skill processes financial table content locally and may receive sensitive cash-flow data.

Mitigation: Run only in a trusted local environment, review inputs before execution, and avoid providing confidential tables unless local execution meets the user's data-handling requirements.

Risk: The free version intentionally omits several checks and does not validate business explanations or forecasting methods.

Mitigation: Use the findings as internal consistency checks only, review omitted checks before relying on the result, and require finance or treasury review for business conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cash-flow-variance-check-free)
- [SkillPay shelf referenced by the artifact](https://skillpay.alipay.com/public/tokendidi)
- [Upgrade and purchase instructions referenced by the artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by the artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON summaries with source-cited findings and local run commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a table with required cash-flow headers; reports insufficient input instead of making conclusions when required evidence is missing.]

## Skill Version(s):

1.0.3 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
