## Description: <br>
Assists users with drafting, revising, reviewing, and generating Word-format Chinese official documents and formal government, institutional, or business materials using Dknowc outline, search, review, and document-formatting workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dknownai](https://clawhub.ai/user/dknownai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers can use this skill to prepare official documents, formal correspondence, reports, notices, meeting minutes, policy-supported materials, and Word or red-header document deliverables. It is intended for formal writing workflows that may require Dknowc search, outline references, source traceability, and human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on Dknowc online services and may ask for a phone number and SMS code during optional agent-assisted registration. <br>
Mitigation: Use agent-assisted registration only with explicit user consent; offer manual MaaS platform setup when the user does not want the agent to handle registration details. <br>
Risk: A resulting API key is stored locally in the installed skill directory. <br>
Mitigation: Keep the key in local configuration only, avoid displaying it, and do not package or publish local config.ini files. <br>
Risk: Formal documents can contain unsupported policy, data, source, or authority claims if generated without review. <br>
Mitigation: Use the skill's search policy, material guidance, source-note workflow, and review checklist before relying on generated official-document content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dknownai/skills/dknownai-official-doc-writer) <br>
- [Dknowc MaaS Platform](https://platform.dknowc.cn/) <br>
- [Dknowc Dependable Search Endpoint](https://open.dknowc.cn/dependable/search/) <br>
- [Task Router](reference/task_router.md) <br>
- [Search Policy](reference/search_policy.md) <br>
- [Material Usage Guidance](reference/material_usage_guidance.md) <br>
- [Output Guide](reference/output_guide.md) <br>
- [Review Checklist](reference/review_checklist.md) <br>
- [Document Standards Index](reference/standards/00_索引.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, configuration steps, .docx files, and HTML source-note files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate ordinary Word documents, red-header Word documents, local initialization/configuration files, search result JSON files, and HTML provenance notes depending on the task.] <br>

## Skill Version(s): <br>
3.2.5 (source: server release evidence and artifact metadata, released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
