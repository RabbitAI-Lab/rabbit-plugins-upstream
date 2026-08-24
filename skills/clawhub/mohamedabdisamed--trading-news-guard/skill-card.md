## Description:

News blackout awareness for trading: local reference for high-impact events (NFP/CPI/FOMC) and blackout-window logic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading automation developers use this skill as guidance for checking high-impact news blackout windows before opening a trade. The skill supports awareness only; the agent or user remains responsible for the trade decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation claims local-only behavior while also describing API-dependent news checks.

Mitigation: Correct the documentation before deployment, or clearly disclose any external API endpoint, network requirement, and exchanged data.

Risk: Users may treat news blackout guidance as enforcement or as a guarantee that trading is safe.

Mitigation: Keep the skill advisory only and require the calling agent or user-defined trading policy to make and log the final trade decision.

Risk: If a real news data source is unavailable or unspecified, the agent may proceed without reliable blackout information.

Mitigation: Configure the calling workflow to fail closed by treating unavailable news status as a blackout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohamedabdisamed/skills/trading-news-guard)
- [Publisher profile](https://clawhub.ai/user/mohamedabdisamed)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, configuration]

**Output Format:** [Markdown guidance with JSON and pseudocode examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable files are included in the submitted artifact.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
