## Description: <br>
深知写作助手 helps agents draft, revise, review, and generate Word-formatted Chinese official documents and formal workplace materials, using DKnowC outline and search services when policy, data, or case support is needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dknownai](https://clawhub.ai/user/dknownai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and document-drafting agents use this skill to prepare Chinese government-style and enterprise formal documents, including notices, reports, requests, replies, meeting minutes, speeches, plans, summaries, and management measures. It can route tasks through drafting, review, DKnowC search, source-note generation, and Word or red-head Word delivery depending on the request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send drafting and search content to DKnowC cloud services. <br>
Mitigation: Use it only for content your organization permits for third-party cloud processing; avoid confidential, classified, personnel, legal, or unreleased internal material unless authorized. <br>
Risk: The skill can register a third-party account and persist an API key in local config.ini. <br>
Mitigation: Run registration only after explicit user consent, keep config.ini out of shared or packaged artifacts, and remove or protect it when the key should no longer be available. <br>
Risk: Generated official documents may include policy, data, or case claims that require review before use. <br>
Mitigation: Review generated documents and source-note HTML before delivery, and verify high-risk factual claims against approved sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-official-doc-writer) <br>
- [README.md](artifact/README.md) <br>
- [Task router](artifact/reference/task_router.md) <br>
- [Search policy](artifact/reference/search_policy.md) <br>
- [Material usage guidance](artifact/reference/material_usage_guidance.md) <br>
- [Output guide](artifact/reference/output_guide.md) <br>
- [Review checklist](artifact/reference/review_checklist.md) <br>
- [DKnowC dependable search endpoint](https://open.dknowc.cn/dependable/search/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses, shell commands, configuration updates, .docx files, and optional HTML source-note files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local Word documents, red-head Word documents, source-note HTML, search result JSON, and local config.ini when the user consents to DKnowC API-key setup.] <br>

## Skill Version(s): <br>
3.2.1 (source: server release evidence, artifact _meta.json, README.md, and CHANGE_log.md released 2026-07-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
