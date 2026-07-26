## Description: <br>
Queries current gasoline and diesel prices for Chinese provinces using TianAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up current 89, 92, 95, and 98 gasoline prices plus 0 diesel prices by Chinese province and return a concise price list. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the user's TianAPI key and province query to TianAPI. <br>
Mitigation: Store the key in TIANAPI_OIL_PRICE_KEY or a secret manager, avoid command-line key passing, and do not commit or share .env files. <br>
Risk: Some documented command examples and JSON-mode guidance may not match the included script behavior. <br>
Mitigation: Test the script before relying on automation and use the supported --key and --prov arguments until the examples and JSON mode are corrected. <br>


## Reference(s): <br>
- [TianAPI Oil Price API](https://www.tianapi.com/apiview/104) <br>
- [ClawHub Skill Page](https://clawhub.ai/workxin/skills/tianapi-oil-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; script output is plain text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a TianAPI API key and a Chinese province name; sends the key and province query to TianAPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
