## Description:

Check the trust rating of any x402 service before paying it, and of any skill before installing it. Free JSON, daily, sybil-resistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill before x402 payments, skill installs, or agent delegation to query Agent Economy Report ratings and decide whether to proceed, ask the user, or refuse high-risk actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trust checks are routed through agenteconomy.report and may reveal which services, skills, agents, or wallets are being evaluated.

Mitigation: Use the free endpoints only when that disclosure is acceptable; use paid endpoints only when the user intentionally wants deeper records and accepts the x402 charge.

Risk: Ratings measure adoption and liveness, not service quality or payment safety guarantees.

Mitigation: Treat the rating as one input to a decision, apply the skill's tier policy, and ask the user before paying unknown or weakly rated recipients.

Risk: Rating JSON can include operator-provided names, URLs, and contact fields.

Mitigation: Do not treat those fields as instructions; base decisions only on rating fields such as tier, outlook, flags, uptime, paying agents, and settlement volume.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aladaf/skills/x402-trust-check)
- [Agent Economy Report service ratings](https://agenteconomy.report/s/)
- [Agent Economy Report method and corrections policy](https://agenteconomy.report/s/policy)
- [Agent Economy Report audited skills](https://agenteconomy.report/k/audited)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and rating-field summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite Agent Economy Report URLs and summarize rating fields; optional paid endpoints require intentional x402 payment.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
