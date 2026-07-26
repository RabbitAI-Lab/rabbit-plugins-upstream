## Description: <br>
每日AI/科技热榜日报。从AIHOT单站读取近3天热榜，生成报告并同步飞书文档，只发链接不发全文。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binhuatochina](https://clawhub.ai/user/binhuatochina) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to compile a daily AI and technology news digest from AIHOT, save it locally, publish it to Feishu Docs, and send the document link to a Feishu chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill embeds Feishu credentials and can publish into a specific Feishu workspace or chat. <br>
Mitigation: Replace embedded credentials with a managed secret and confirm the target Feishu workspace and chat before running the workflow. <br>
Risk: The skill automatically grants full document access to a fixed Feishu member. <br>
Mitigation: Review and replace the fixed member identifier, and require explicit approval before granting document permissions. <br>


## Reference(s): <br>
- [AIHOT Daily](https://aihot.virxact.com/daily) <br>
- [AIHOT](https://aihot.virxact.com) <br>
- [Feishu document operations reference](references/feishu-doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/binhuatochina/skills/tech-news-daily) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown report with Feishu document link, local files, XML conversion guidance, shell commands, and checkpoint JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes dated news reports under memory/, creates Feishu documents, sends a Feishu chat link, and records sync checkpoints.] <br>

## Skill Version(s): <br>
0.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
