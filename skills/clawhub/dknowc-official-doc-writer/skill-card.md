## Description: <br>
深知公文写作 helps agents draft, revise, review, and produce Word-format Chinese official documents and formal institutional materials using DKnowC outline, search, formatting, and review workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ClawHub users and organizational staff can use this skill to prepare Chinese official documents, formal correspondence, meeting materials, reports, notices, and related Word deliverables. The skill routes tasks through drafting, DKnowC search, source review, formatting, and red-header document generation when those steps are appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Assisted setup sends the user's phone number and SMS code to DKnowC to create or provision API access. <br>
Mitigation: Use assisted setup only with user consent, or configure API access manually through the DKnowC MaaS platform. <br>
Risk: The DKnowC API key is stored locally in the skill's config.ini. <br>
Mitigation: Keep config.ini local, exclude it from published artifacts, and rotate the key if it is exposed. <br>
Risk: Drafting prompts and search queries may be sent to DKnowC services. <br>
Mitigation: Do not submit confidential government, enterprise, personnel, or regulated content unless DKnowC is approved for that use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer) <br>
- [README](artifact/README.md) <br>
- [Search Policy](artifact/reference/search_policy.md) <br>
- [Material Usage Guidance](artifact/reference/material_usage_guidance.md) <br>
- [Output Guide](artifact/reference/output_guide.md) <br>
- [Review Checklist](artifact/reference/review_checklist.md) <br>
- [Official Document Standards Index](artifact/reference/standards/00_索引.md) <br>
- [DKnowC MaaS Platform](https://platform.dknowc.cn/) <br>
- [DKnowC Dependable Search Endpoint](https://open.dknowc.cn/dependable/search/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, generated .docx files, HTML source notes, JSON search or outline artifacts, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local initialization, configured DKnowC API access, and Python dependencies before drafting, search, Word, red-header, or source-note workflows can run.] <br>

## Skill Version(s): <br>
3.2.5 (source: release evidence and artifact/_meta.json; changelog released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
