## Description: <br>
Uses the ClawEC API to analyze Amazon ABA market trends by marketplace, month, category, search mode, and optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, ecommerce operators, and agents use this skill to submit ClawEC Amazon ABA market-trend searches, review search logs and details, and summarize keyword, brand, purchase-rate, and optional AI interpretation results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ClawEC API key and can return account/search logs containing market research history. <br>
Mitigation: Provide CLAWEC_API_KEY only through the environment, avoid hardcoding or sharing it, and review returned logs before redistributing outputs. <br>
Risk: The helper scripts send Amazon ABA search parameters to the ClawEC service. <br>
Mitigation: Install and run the skill only when ClawEC is the intended service for the analysis and the queried marketplace data can be shared with that service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-aba-selection) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC account registration](https://www.clawec.com/?source=q-clawhub) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Chinese summaries and guidance with shell command examples; helper scripts return JSON and optional Markdown AI analysis.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY for ClawEC API access; optional polling is controlled by MT_POLL_INTERVAL and MT_POLL_MAX.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
