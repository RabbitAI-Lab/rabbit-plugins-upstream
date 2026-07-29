## Description: <br>
将用户已授权账号中的抖音收藏配置并同步到本地 Markdown 或 Obsidian 知识库；提供首次 setup、增量 sync、登录恢复、JSON 导入、局部审核，以及按需接入本地转录、MiniMax 或其他分析模型和飞书通知。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tars1230](https://clawhub.ai/user/tars1230) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure an authorized Douyin account workflow and sync newly approved favorites into a local Markdown or Obsidian knowledge base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing and running the referenced Python CLI can execute local code and create persistent local state. <br>
Mitigation: Review the referenced source and install only in a user-approved project directory or isolated environment. <br>
Risk: The workflow stores a local browser login profile and can write approved favorites into the selected knowledge base. <br>
Mitigation: Use the default confirmed sync flow first, keep cookies and browser profiles private, and only approve writes after reviewing the proposed changes. <br>
Risk: Unattended sync, model adapters, transcription, and Feishu notifications can expand data flows beyond the default local workflow. <br>
Mitigation: Enable --yes, adapters, transcription, or notifications only after the user explicitly requests those behaviors and understands the data exposure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tars1230/skills/douyin-favorites-to-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with inline bash command blocks and configuration choices] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-authorized Douyin login and explicit approval before normal sync writes to the local knowledge base.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
