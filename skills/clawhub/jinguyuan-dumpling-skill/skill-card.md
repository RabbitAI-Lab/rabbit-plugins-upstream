## Description: <br>
金谷园饺子馆信息查询、匿名实体抽奖卡与在线排队取号。通过金谷园官方 API 查询店铺、排队和菜品信息；可揭晓抽奖卡并当场匿名交付兑奖码（一次性发放，无需登录）、凭本地凭证查询已领奖品；内置真实排队动作仅用于在线取号、本人排队进度查询、取消排队。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinguyuan](https://clawhub.ai/user/jinguyuan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to answer questions about 金谷园饺子馆, check queue status, retrieve anonymous prize-card results, and manage online queue numbers with explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Online queue actions can use account-linked Meituan authorization and store local auth, claim, QR, or polling state. <br>
Mitigation: Use queue actions only after explicit user confirmation, review the local persistence behavior before deployment, and clear local authorization when it is no longer needed. <br>
Risk: The bundled Meituan signing dependency is reported by the security evidence as including under-disclosed device fingerprinting. <br>
Mitigation: Install or enable online queueing only in environments where that account-linked behavior is acceptable; otherwise restrict use to public restaurant queries. <br>


## Reference(s): <br>
- [Public Query API Reference](references/api-reference.md) <br>
- [Queue Actions Reference](references/queue-actions.md) <br>
- [Queue Reply Contract](references/queue-reply-contract.md) <br>
- [金谷园饺子馆 Skill on ClawHub](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill) <br>
- [金谷园官网](https://jinguyuan.cloud) <br>
- [金谷园 MCP Endpoint](https://mcp.jinguyuan.cloud) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and JSON CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Public restaurant queries use official API snapshots; online queue actions require explicit user confirmation and local authorization.] <br>

## Skill Version(s): <br>
3.1.0 (source: SKILL.md frontmatter, skill.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
