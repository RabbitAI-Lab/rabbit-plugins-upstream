## Description: <br>
保存、搜索和管理 Get笔记个人笔记与知识库，并仅在用户明确要求操作得到大脑或 Get笔记时启用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iswalle](https://clawhub.ai/user/iswalle) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to connect to Get笔记 and intentionally save, search, organize, edit, delete, and share notes or knowledge-base content from a personal account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private notes, search terms, links, images, audio transcripts, and knowledge-base details may be sent to Get笔记 cloud services. <br>
Mitigation: Invoke the skill only after explicit user intent, disclose data sharing before first authorization, and send credentialed requests only to https://openapi.biji.com. <br>
Risk: Stored API credentials could allow account access if exposed or used by the wrong participant. <br>
Mitigation: Keep credentials in environment or configured skill storage, avoid displaying API keys in chat, and use GETNOTE_OWNER_ID to restrict operation in shared contexts. <br>
Risk: Delete, tag removal, knowledge-base removal, or public sharing actions can change or expose user content. <br>
Mitigation: Show the target object and require explicit confirmation before destructive actions or public share-link creation; default to private internal links. <br>
Risk: Incorrect or premature status claims could mislead users about saved, deleted, or updated notes. <br>
Mitigation: Treat API responses as the source of truth, never fabricate note IDs or success responses, and poll asynchronous save tasks until success or failure. <br>


## Reference(s): <br>
- [Get笔记 Skill Page](https://clawhub.ai/iswalle/skills/getnote) <br>
- [Publisher Profile](https://clawhub.ai/user/iswalle) <br>
- [Get笔记 Homepage](https://biji.com) <br>
- [Get笔记 OpenAPI](https://openapi.biji.com) <br>
- [Get笔记 API 详细参考](references/api-details.md) <br>
- [授权配置](references/oauth.md) <br>
- [保存笔记](references/save.md) <br>
- [语义搜索](references/search.md) <br>
- [笔记列表与详情](references/list.md) <br>
- [知识库管理](references/knowledge.md) <br>
- [标签管理](references/tags.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown text with API guidance, command examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include note IDs, search results, status messages, private internal note links, or public share links after explicit confirmation.] <br>

## Skill Version(s): <br>
1.9.1 (source: package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
