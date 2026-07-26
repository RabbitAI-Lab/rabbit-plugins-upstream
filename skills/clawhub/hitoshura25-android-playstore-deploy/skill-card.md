## Description: <br>
一个帮助开发者设置自动化Google Play商店部署流程的工具，支持项目分析、密钥生成、服务账户配置和GitHub Actions工作流生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release engineers use this skill to prepare Android projects for Google Play deployment, including project analysis, signing setup, service account guidance, GitHub Actions workflow generation, and deployment validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for high-value Android deployment credentials and deployment data that may be sent to xiaobenyang.com. <br>
Mitigation: Use disposable or least-privilege credentials, avoid production signing keys and broad GitHub PATs, and review any deployment data before using the skill. <br>
Risk: The skill may store an API key in a local .env file. <br>
Mitigation: Protect the .env file from source control or sharing, and remove or rotate the API key when you stop using the skill. <br>
Risk: Server security evidence reports weak disclosure and mismatched documentation. <br>
Mitigation: Review remote API results, generated configuration, and deployment instructions before applying them to production projects. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/hitoshura25-android-playstore-deploy) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with generated code, configuration snippets, shell commands, and remote API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated Android signing configuration, GitHub Actions workflow content, setup steps, validation results, and deployment test guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
