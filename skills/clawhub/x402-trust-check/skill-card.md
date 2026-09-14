## Description:

Check the trust rating of any x402 service before paying it, and of any skill before installing it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to check x402 services, skill releases, and other agents before paying, installing, or delegating to them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on agenteconomy.report as an external trust source for x402 payment and installation decisions.

Mitigation: Use the rating as supporting evidence rather than a guarantee, and apply the user's risk tolerance before paying or installing.

Risk: The optional conduct arena can submit agent name/version information and return an externally supplied briefing.

Mitigation: Run it only after explicit operator approval, and review each resulting action before any payment, credential disclosure, or unrelated tool use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aladaf/skills/x402-trust-check)
- [Agent Economy Report service ratings](https://agenteconomy.report/s/)
- [Agent Economy Report method and corrections policy](https://agenteconomy.report/s/policy)
- [Audited skills index](https://agenteconomy.report/k/audited)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Analysis]

**Output Format:** [Markdown with inline bash commands and concise risk recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference free JSON rating endpoints and optional paid x402 audit or history endpoints.]

## Skill Version(s):

1.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
