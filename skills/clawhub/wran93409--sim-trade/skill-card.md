## Description:

Sim Trade provides an A-share stock trading simulator for quote lookup, local virtual trading, position tracking, trade logs, and account summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wran93409](https://clawhub.ai/user/wran93409)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use Sim Trade to practice A-share stock trading with local virtual funds, query market quotes, and review account, position, and trade history outputs. Users should treat it as a simulator and not as investment advice or a verified broker integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes simulated account state under ~/.openclaw/sim_trade and contacts Tencent for stock quotes.

Mitigation: Install and run it only when local account-state files and outbound quote requests are acceptable for the deployment environment.

Risk: The security evidence warns that users are asked to store financial cookies or broker API tokens insecurely.

Mitigation: Prefer local simulation mode, avoid placing real broker tokens or browser cookies in config.json, and protect any configuration file that contains account credentials.

Risk: The security evidence says advertised real-account sync is not actually implemented in the inspected code.

Mitigation: Treat real-account sync as unavailable unless separately reviewed, implemented, and tested against the intended provider.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wran93409/skills/sim-trade)
- [Tencent Quote Endpoint](https://qt.gtimg.cn/q={market}{code})
- [Eastmoney Simulation Trading](https://simup.eastmoney.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and terminal text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local account, position, quote, and trade-history outputs; no public evaluation artifacts were provided.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact/skill.json lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
