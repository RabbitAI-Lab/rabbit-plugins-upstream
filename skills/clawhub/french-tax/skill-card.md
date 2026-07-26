## Description: <br>
一个提供法国个人所得税计算的MCP服务器，支持基于净应税收入和家庭构成的计算，并动态获取最新税档信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to calculate French income tax and retrieve tax brackets, form details, deadlines, procedures, and law article information through a XiaoBenYang-backed API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends tax inputs to a third-party API with limited disclosure and weak scoping. <br>
Mitigation: Use only if that processor is acceptable, and avoid entering unnecessary personal tax details. <br>
Risk: The skill stores the XBY_APIKEY in a local plaintext .env file. <br>
Mitigation: Protect the workspace and remove the saved XBY_APIKEY when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/french-tax) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [JSON API results summarized as text or Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY; can generate Markdown reports for requested tax topics.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata); artifact frontmatter says 1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
