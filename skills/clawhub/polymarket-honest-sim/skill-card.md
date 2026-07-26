## Description: <br>
Build, paper-trade, and honestly backtest Polymarket-style trading bots on PaperBook, a paper-money CLOB with Polymarket-compatible APIs and a simulator that replays recorded Polymarket order books with honest fills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johanalvarado](https://clawhub.ai/user/johanalvarado) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-strategy builders use this skill to integrate bots with PaperBook, run live paper trades, and backtest prediction-market strategies against recorded order books. It helps agents report simulation results using the honest fillable lens, certificate, and reproducibility hash rather than presenting naive paper performance as real edge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to contact paperclob.com and create or use paper-trading credentials. <br>
Mitigation: Store generated API keys, secrets, and passphrases in a local secret store or environment file, avoid logging them, and never commit them to source control. <br>
Risk: The skill may lead an agent to produce integration code against a changing external API. <br>
Mitigation: Fetch https://paperclob.com/llms-full.txt before coding and treat it as the current contract for endpoints, authentication, order shapes, and validation checks. <br>
Risk: Paper-trading or simulation results may be mistaken for evidence of live-market profitability. <br>
Mitigation: Report results as paper-testing evidence only, lead with the honest_fillable lens and verdict, include the certificate and reproducibility hash, and avoid claiming real-market profitability. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/johanalvarado/skills/polymarket-honest-sim) <br>
- [PaperBook](https://paperclob.com) <br>
- [PaperBook Current API Contract](https://paperclob.com/llms-full.txt) <br>
- [PaperBook Blog](https://paperclob.com/blog) <br>
- [PaperBook reference - stable concepts](reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code blocks, API request examples, and implementation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to fetch the current PaperBook contract before producing integration code; paper-trading credentials and simulation reports should be handled as sensitive task artifacts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
