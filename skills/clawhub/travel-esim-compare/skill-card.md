## Description: <br>
出境上网比价助手，支持eSIM套餐比价和WiFi租借查询，覆盖Airalo/Holafly等主流运营商和30+热门目的地，零配置即装即用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers use this skill to compare built-in eSIM plans, WiFi rental options, and data-use guidance for international destinations before choosing a connectivity option. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports unnecessary PROXY_TOKEN access and a hardcoded token-like fallback. <br>
Mitigation: Review before installing and ask the publisher to remove the token access and fallback or document why they are required. <br>
Risk: Built-in travel connectivity prices and availability can become outdated. <br>
Mitigation: Confirm current plan details with the provider before purchase and treat the skill output as comparison guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-esim-compare) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON strings and concise Chinese travel connectivity guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses built-in destination, provider, price, WiFi rental, and phone compatibility data.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
