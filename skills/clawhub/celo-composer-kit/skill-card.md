## Description: <br>
Celo MCP Server 是一个用于安装和配置 Celo Composer Kit MCP 服务器的工具，支持在 macOS 上运行，提供组件发现、集成和示例功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to query Celo Composer Kit component documentation, examples, props, categories, installation guidance, and CLI create-command information through the configured XiaoBenYang API service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is advertised as a Celo helper, but it requires a XiaoBenYang API key and sends requests to a XiaoBenYang remote service. <br>
Mitigation: Use it only when you intend to use XiaoBenYang's service, and confirm the endpoint and credential purpose before providing an API key. <br>
Risk: The API key is saved in a plaintext .env file. <br>
Mitigation: Use a dedicated revocable key, protect the workspace where the .env file is stored, and rotate or remove the key when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/celo-composer-kit) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses summarizing JSON API results, with code or shell command snippets when relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided tool parameters and a required XiaoBenYang API key.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
