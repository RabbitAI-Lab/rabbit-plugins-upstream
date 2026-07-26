## Description: <br>
Queries real-time gold, silver, and other precious-metal market data, including buy and sell prices, highs and lows, and percentage change. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve structured TianAPI precious-metal quotes through an agent workflow or the bundled Python script. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The TianAPI key is a secret and may be exposed if passed directly on the command line or committed in scripts/.env. <br>
Mitigation: Prefer TIANAPI_GOLD_KEY as an environment variable, avoid command-line key arguments when possible, and keep any .env file out of version control. <br>


## Reference(s): <br>
- [TianAPI Gold Price API](https://www.tianapi.com/apiview/146) <br>
- [TianAPI Gold API Endpoint](https://apis.tianapi.com/gold/index) <br>
- [ClawHub Skill Page](https://clawhub.ai/workxin/skills/tianapi-gold-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TIANAPI_GOLD_KEY; supports one or more comma-separated precious-metal kind codes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
