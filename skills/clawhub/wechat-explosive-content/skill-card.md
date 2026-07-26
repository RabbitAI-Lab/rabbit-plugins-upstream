## Description: <br>
Searches Redfox-backed WeChat Official Account hot articles by keyword, ranks viral content, and helps creators find topic inspiration and trend signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, WeChat operators, brand teams, and self-media teams use this skill to search recent high-read WeChat articles, compare trends, and plan topics. It can also guide an agent to run the bundled Python script and present the returned data as tables, recommendations, or optional reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search keywords and requests are sent to Redfox. <br>
Mitigation: Use the skill only when sharing those keywords with Redfox is acceptable, and avoid sensitive search terms. <br>
Risk: The skill requires a REDFOX_API_KEY. <br>
Mitigation: Use a revocable key, confirm its scope and validity period, and avoid exposing it in prompts, logs, code, or generated files. <br>
Risk: Reference documentation includes an apparent plaintext API key. <br>
Mitigation: Do not reuse the documented key; the publisher should remove and rotate it. <br>
Risk: The subscription flow can create persistent scheduled pushes. <br>
Mitigation: Review any calendar subscription before accepting it and confirm how to cancel scheduled pushes. <br>


## Reference(s): <br>
- [Skill listing](https://clawhub.ai/redfox-data/skills/wechat-explosive-content) <br>
- [English README](README.en.md) <br>
- [WeChat trend data format](references/gzh_trend_data_format.md) <br>
- [RedFox](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown tables and guidance, with optional JSON or HTML report output from the bundled script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; may guide optional calendar subscription creation after search results.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
