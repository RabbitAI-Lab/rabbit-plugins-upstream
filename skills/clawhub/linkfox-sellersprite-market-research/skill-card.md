## Description: <br>
Screens and ranks Amazon category markets with SellerSprite data across market size, competition, concentration, seller structure, new-product share, pricing, ratings, and profit filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to research Amazon category opportunities with SellerSprite data, compare candidate markets, and guide product-selection decisions before making paid API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid-credit API calls can incur costs. <br>
Mitigation: Confirm the user wants to proceed before repeat calls, retries, pagination, or broadened searches. <br>
Risk: API credentials and request routing are sensitive. <br>
Mitigation: Use trusted LinkFox/SellerSprite credentials and keep LINKFOX_TOOL_GATEWAY unset unless the destination is controlled and expected. <br>
Risk: Full market-research responses are stored locally. <br>
Mitigation: Review saved response files for sensitive business data and remove them when they are no longer needed. <br>
Risk: Automatic feedback reporting and onboarding installation may send data or add another skill. <br>
Mitigation: Review or disable feedback behavior and install the onboarding package only when intentionally needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-market-research) <br>
- [SellerSprite market research API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell command examples, and JSON API responses or summarized JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved locally; responses over 8 KB are summarized unless inline output is requested; repeated calls may consume paid credits.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
