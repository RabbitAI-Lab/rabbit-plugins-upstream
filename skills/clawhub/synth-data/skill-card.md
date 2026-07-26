## Description: <br>
Query volatility forecasts from Synthdata.co for crypto, commodities, and stocks. Compare assets and run Monte Carlo simulations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emsin44](https://clawhub.ai/user/emsin44) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and trading workflow builders use this skill to query Synthdata volatility forecasts, compare supported assets, generate Monte Carlo price ranges, and prepare alert or reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Synthdata API key, which could be exposed through shared terminals, logs, or copied shell history. <br>
Mitigation: Use a revocable Synthdata key, provide it through the environment only for intended runs, and avoid printing or sharing the key in logs or transcripts. <br>
Risk: Selected asset tickers are sent to Synthdata during API queries. <br>
Mitigation: Run the skill only when sending those ticker queries to Synthdata is acceptable, and review any scheduled report, Slack, Telegram, or alert integrations before enabling them. <br>
Risk: Volatility forecasts and Monte Carlo ranges can be mistaken for deterministic trading advice. <br>
Mitigation: Treat outputs as analytical signals, validate assumptions independently, and apply human review before using them for trading, alerts, or portfolio decisions. <br>


## Reference(s): <br>
- [Synthdata API Reference](artifact/references/api.md) <br>
- [Synthdata](https://synthdata.co) <br>
- [ClawHub Skill Page](https://clawhub.ai/emsin44/skills/synth-data) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text tables and optional JSON, with shell commands and configuration guidance in Markdown documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and SYNTHDATA_API_KEY; outbound API requests send selected asset tickers to Synthdata.] <br>

## Skill Version(s): <br>
1.1.5 (source: ClawHub release metadata and clawhub.json, released 2026-02-12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
