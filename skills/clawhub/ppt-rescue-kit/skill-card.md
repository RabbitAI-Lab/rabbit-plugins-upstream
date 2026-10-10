## Description:

Creates or repairs an editable PowerPoint deck from a topic or unfinished presentation, with slide copy, speaker notes, citations, and JishuDB records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Professionals preparing work updates, proposals, and talks use this skill to create or finish editable presentations with speaker notes and source citations. It retains supporting records in an authorized JishuDB knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional JishuDB Desktop setup can change the local app, data paths, and agent connection configuration.

Mitigation: Review the displayed setup plan, installer source, paths, MCP endpoint, and write permissions before approving; decline setup if local PPT files alone are desired.

Risk: Presentation sources and drafts may be retained in JishuDB.

Mitigation: Confirm the selected knowledge base and consent to retain the specific source and output materials before writing.

Risk: Unsupported claims or invented chart data could mislead presentation readers.

Mitigation: Map factual claims to inspected sources and mark assumptions or unsupported data instead of inventing figures.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/ppt-rescue-kit)
- [Skill homepage (release metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/ppt-rescue-kit)
- [Bundled JishuDB setup](references/jishudb-setup/setup.md)
- [JishuDB installation contract](references/jishudb-setup/references/installation-contract.md)
- [Task execution defaults](references/jishudb-setup/task-execution.md)

## Skill Output:

**Output Type(s):** [Files, Markdown documents]

**Output Format:** [Editable .pptx deck with Markdown slide notes, sources, and revision record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supporting source, draft, final, and revision records are retained in an authorized JishuDB knowledge base.]

## Skill Version(s):

0.1.5 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
