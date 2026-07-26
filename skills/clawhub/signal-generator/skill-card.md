## Description: <br>
Generate trading signals using BB Breakout or RSI Reversal strategies and prepare signal output for optional alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nititepfirm](https://clawhub.ai/user/nititepfirm) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and trading-automation users can run this skill to generate technical trading signals for configured symbols and timeframes. The output can be reviewed directly or connected to separate alerting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can be scheduled through cron and depends on a trusted local /root/quant-trading-bot environment when that environment is present. <br>
Mitigation: Verify the local trading-bot environment before installation and add recurring cron execution only when repeated signal generation is intended. <br>
Risk: Trading signal details may be shared with third-party messaging services if a separate alerting wrapper is connected. <br>
Mitigation: Use dedicated alert channels and confirm what signal data will be sent before enabling Discord, Telegram, or custom messaging integrations. <br>
Risk: Generated trading signals can be mistaken for financial advice. <br>
Mitigation: Review outputs as technical indicators only and require human judgment before making trading decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nititepfirm/skills/signal-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Console text with markdown-style signal messages and JSON signal files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes latest generated signals to last_signal.json when signals are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
