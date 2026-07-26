## Description: <br>
通过Amazon Q CLI和MCP服务器在GitHub Codespace中快速生成高质量的AWS架构图。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud architects use this skill to create AWS and related architecture diagrams by selecting diagram tools, generating diagram code, listing available icons, and returning generated diagram results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires and persists an XBY API key in a workspace .env file. <br>
Mitigation: Use a scoped API key, avoid workspaces with unrelated secrets, and remove the .env entry when the skill is no longer needed. <br>
Risk: Diagram prompts and generated diagram code are sent to an external Xiaobenyang service. <br>
Mitigation: Do not submit confidential architecture details unless the publisher clarifies the service identity, storage behavior, and remote data flow. <br>
Risk: Server security evidence marks the release suspicious because the AWS diagram label conflicts with Xiaobenyang API behavior and leftover Gaokao references. <br>
Mitigation: Review the artifact and publisher trust signals before installing or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/awslabs-aws-diagram) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP service endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON-like tool results, including generated diagram paths when successful] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require an XBY API key and may save generated diagram files in the workspace.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
