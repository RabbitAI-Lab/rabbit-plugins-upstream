## Description: <br>
一个智能Logo提取和处理的MCP服务器，支持从网站URL自动识别并提取Logo图标，并提供图像处理和矢量转换功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to extract the best logo URL from a website or request basic logo analysis such as dimensions, format, and quality through the XiaoBenYang service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires trust in the XiaoBenYang service and sends logo-analysis requests to that external API. <br>
Mitigation: Install only if that service is acceptable for the intended use, and avoid submitting sensitive or private URLs unless permitted by your organization. <br>
Risk: The required API key may be stored persistently in a local .env file as XBY_APIKEY. <br>
Mitigation: Use a dedicated low-privilege key where possible, protect the .env file, and remove or rotate the key when the skill is no longer needed. <br>
Risk: Server security evidence notes copy-paste documentation and configuration mismatches. <br>
Mitigation: Review the documented tool behavior and local configuration before installation, especially the required API-key setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/logo-analyze) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown or plain text summarizing JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw API data with success status and message fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
