## Description: <br>
基于JSXGraph的MCP协议服务器，提供13种数学可视化工具，适用于教育数学、工程和科学应用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, educators, and technical users use this skill to generate JSXGraph-backed mathematical visualizations for teaching, engineering, and scientific analysis. It routes chart requests to a remote XiaoBenYang MCP API and returns the service response for presentation to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and stores XBY_APIKEY in a local .env file. <br>
Mitigation: Keep the .env file out of source control and shared archives, and rotate the key if it may have been exposed. <br>
Risk: Visualization inputs and tool parameters are sent to the remote XiaoBenYang service. <br>
Mitigation: Avoid sending confidential or regulated data unless the service terms and data handling are acceptable for the intended use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/mathematical-visualization) <br>
- [XiaoBenYang API key and service site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, API Calls, configuration, guidance] <br>
**Output Format:** [Markdown or structured JSON summaries of remote visualization API responses, with code/configuration guidance when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY credential and network access to the XiaoBenYang visualization service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
