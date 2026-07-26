## Description: <br>
Helps agents use LinkFox gateway scripts and references for Temu EU Partner Ads APIs, including ad creation, modification, reporting, logs, eligible-goods lookup, and ROAS prediction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to run Temu EU Ads workflows through LinkFox, including creating or modifying ads, checking eligible goods, predicting ROAS, and retrieving reports. It is intended for users who already have appropriate LinkFox and Temu credentials. <br>

### Deployment Geography for Use: <br>
Europe <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles LinkFox and Temu credentials, including optional local storage of Temu access tokens. <br>
Mitigation: Use short-lived, least-privilege tokens through environment variables when possible, avoid plaintext local token storage for shared machines, and do not run token-listing or token-get scripts in logged sessions. <br>
Risk: The Ads scripts can create or modify live Temu advertising campaigns and may affect spend, budget, ROAS targets, or ad status. <br>
Mitigation: Review every request payload before execution, prefer the Ads-specific scripts over the arbitrary proxy, and require operator approval for spend-affecting changes. <br>
Risk: Saved API response files may contain business-sensitive account, campaign, or report data. <br>
Mitigation: Store response files only in approved project directories, review them before sharing, and delete or redact sensitive outputs after use. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-eu) <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization and setup](references/access-token.md) <br>
- [Partner EU Ads interface catalog](references/partner-eu-catalog.md) <br>
- [Ads API document index](references/apis/README.md) <br>
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request or response examples; scripts may write JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Large API responses are summarized on stdout while full JSON is written to a local linkfox output directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
