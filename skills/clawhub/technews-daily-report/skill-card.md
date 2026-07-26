## Description: <br>
每日AI/科技热榜日报。从AIHOT单站读取近3天热榜，生成报告并同步飞书文档，只发链接不发全文。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binhuatochina](https://clawhub.ai/user/binhuatochina) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to generate a daily AI and technology news digest from AIHOT, save the report locally, publish it to a Feishu document, and send the document link to a Feishu chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports embedded Feishu credentials and raw API calls that grant document access. <br>
Mitigation: Rotate the exposed secret, remove hard-coded credentials before installation, and use a managed Feishu integration or environment-based secret handling. <br>
Risk: The workflow can create Feishu documents, grant permissions, and send a message to a fixed chat automatically. <br>
Mitigation: Require explicit user confirmation before document creation, permission grants, and message sending; verify the target space, recipient, and chat before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binhuatochina/skills/technews-daily-report) <br>
- [AIHOT](https://aihot.virxact.com) <br>
- [AIHOT daily feed](https://aihot.virxact.com/daily) <br>
- [Feishu document operations reference](references/feishu-doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown report, Feishu document link, local Markdown/XML files, and checkpoint JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates dated local report and checkpoint files, updates a Feishu document, and sends a Feishu message containing the document link.] <br>

## Skill Version(s): <br>
0.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
