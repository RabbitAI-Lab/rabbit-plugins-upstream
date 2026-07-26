## Description: <br>
OPC全领域指南为代理提供 OPC Classic 和 OPC UA 的概念、入门、开发、PLC 集成、安全配置、故障排查、配套规范和工具选型指导。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and industrial automation engineers use this skill to get Chinese-language OPC Classic and OPC UA explanations, setup steps, code examples, PLC integration guidance, security configuration advice, troubleshooting paths, and tool or SDK selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lab-only insecure OPC UA examples such as None security mode, auto-accepted certificates, or useSecurity:false may be copied into production or shared industrial networks. <br>
Mitigation: Use those examples only in isolated test environments; for real deployments use verified certificates, SignAndEncrypt, and production security policies. <br>
Risk: Generated OPC UA private keys can expose an application identity if they are mishandled. <br>
Mitigation: Store generated private keys with restricted access, avoid committing or sharing them, and rotate credentials according to the deployment policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/skills/opc-guide) <br>
- [OPC UA 入门指南](references/opc-ua-setup.md) <br>
- [OPC 核心概念速查](references/opc-ua-concepts.md) <br>
- [OPC UA PLC 集成指南](references/opc-ua-plc-integration.md) <br>
- [OPC UA 安全配置指南](references/opc-ua-security.md) <br>
- [OPC UA 故障排查手册](references/opc-ua-troubleshooting.md) <br>
- [OPC UA 配套规范速查](references/opc-ua-companion-specs.md) <br>
- [OPC UA 工具与 SDK 速查](references/opc-ua-tools.md) <br>
- [OPC Foundation developer documents](https://opcfoundation.org/developer-tools/documents) <br>
- [Prosys OPC UA Simulation Server](https://www.prosysopc.com/products/opc-ua-simulation-server/) <br>
- [Unified Automation UaExpert](https://www.unified-automation.com/products/development-tools/uaexpert.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown responses; complex scenarios may include HTML reports with code blocks and SVG diagrams.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-first answers with reference links; the helper script can produce console output for OPC UA checks and certificate generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
