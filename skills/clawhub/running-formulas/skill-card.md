## Description: <br>
一个提供全面的跑步计算工具的MCP服务器，包括VDOT计算、训练配速、比赛时间预测、速度标记、心率区间和配速转换等功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External runners, coaches, and agents use this skill to calculate running performance metrics, training paces, race predictions, heart-rate zones, and pace or speed conversions through a remote MCP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for and stores an API key in a local .env file. <br>
Mitigation: Install only if you trust the remote service, limit access to the stored key, and delete the key when it is no longer needed. <br>
Risk: The skill sends running inputs and the API key to a remote xiaobenyang.com service. <br>
Mitigation: Avoid submitting sensitive inputs and review whether remote processing is acceptable before use. <br>
Risk: The security summary notes mismatched copied Gaokao-related code and documentation, making the true scope harder to review. <br>
Mitigation: Review the artifact files and restrict direct use of scripts.call_api until the mismatch is resolved or accepted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/running-formulas) <br>
- [Publisher profile](https://clawhub.ai/user/cainingnk) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown summaries of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value and sends calculation parameters to the remote XiaoBenYang MCP API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
