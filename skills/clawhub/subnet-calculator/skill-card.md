## Description: <br>
一个基于Model Context Protocol的服务，提供IPv4子网规划工具，包括子网大小计算、通配符掩码生成、网关选择和主机验证等功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Network engineers, developers, and operations teams use this skill to calculate IPv4 subnet sizing, wildcard masks, subnet membership, subnet mask details, and usable host addresses through the configured XiaoBenYang API service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for an API key and stores it in a local .env file in plaintext. <br>
Mitigation: Use a scoped API key where possible, restrict workspace access, avoid shared environments, and remove the .env entry when the skill is no longer needed. <br>
Risk: Subnet calculation inputs are routed to the external xiaobenyang.com service. <br>
Mitigation: Do not submit sensitive internal network data unless the provider is approved for that data; use an offline subnet calculator when external routing is not acceptable. <br>
Risk: The artifact includes leftover unrelated gaokao or school-search wording, which may confuse review or operation. <br>
Mitigation: Review the skill instructions before deployment and test only the documented subnet tool paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/subnet-calculator) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, configuration guidance] <br>
**Output Format:** [Markdown text summarizing JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value before API-backed subnet calculations can run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
