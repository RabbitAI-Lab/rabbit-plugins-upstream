## Description: <br>
上市公司合规、任职资格、公司治理及信息披露咨询，使用 hegui 数据库法规正文和公告原文件来形成来源受限的合规答复。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and compliance practitioners use this skill to ask whether listed-company events are compliant, require disclosure, affect director or executive eligibility, or need announcement formats and comparable disclosure examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The hegui MCP token is placed in local agent configuration and compliance questions are sent to that MCP service. <br>
Mitigation: Install only when this data flow is acceptable, protect the token, and prefer non-identifying facts unless identification is necessary for the consultation. <br>
Risk: Source boundaries can broaden if an external-source fallback is intentionally used. <br>
Mitigation: For strict source control, rely only on hegui database records and their original attachments, and do not use external-source fallback behavior. <br>
Risk: Unsupported compliance conclusions can result if excerpts, internal routing fields, or announcement cases are treated as legal authority. <br>
Mitigation: Use only current, complete regulation text that passes the skill's evidence gates; keep announcement cases as practice references and do not use them to infer legal conclusions. <br>


## Reference(s): <br>
- [Skill source](SKILL.md) <br>
- [Installation and MCP setup](INSTALL.md) <br>
- [Routing contract](references/routing-contract.md) <br>
- [Citation standard](references/citation-standard.md) <br>
- [Full-text verification](references/full-text-verification.md) <br>
- [Retrieval strategy](references/retrieval-strategy.md) <br>
- [Answer contract](references/answer-contract.md) <br>
- [Announcement retrieval](references/announcement-retrieval.md) <br>
- [Format retrieval](references/format-retrieval.md) <br>
- [Clarification policy](references/clarification-policy.md) <br>
- [Evaluation cases](references/evaluation-cases.md) <br>
- [ClawHub skill page](https://clawhub.ai/zoeluli7459-dev/skills/hegui) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Structured Markdown answer with conclusions, legal basis, clause text, applicability analysis, announcement formats, and verified announcement case references when available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Answers are source-bound to the configured hegui database records and their original attachments; the skill should not supplement regulations or announcements from independent web search or model memory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
