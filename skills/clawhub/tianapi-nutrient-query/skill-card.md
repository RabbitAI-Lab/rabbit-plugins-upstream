## Description: <br>
查询近两千种常见食物的详细营养成分，支持按食品名称、分类或特定营养素进行检索和排序。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query TianAPI nutrition data for foods, food categories, or nutrient rankings, then present the returned nutrition facts in a readable response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A TianAPI account key may be exposed if it is passed on the command line, placed in shared URLs, or committed in scripts/.env. <br>
Mitigation: Store the key in TIANAPI_NUTRIENT_KEY or a protected secret store, avoid shared command histories and URLs containing the key, and exclude scripts/.env from source control. <br>
Risk: Current CLI examples and documentation may require adjustment before the helper script works reliably. <br>
Mitigation: Test the helper script with a non-sensitive query before relying on it, and prefer the documented environment variable configuration path. <br>


## Reference(s): <br>
- [TianAPI Nutrient API documentation](https://www.tianapi.com/apiview/121) <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-nutrient-query) <br>
- [Publisher profile](https://clawhub.ai/user/workxin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a TianAPI nutrient API key configured as TIANAPI_NUTRIENT_KEY or supplied to the helper script.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
