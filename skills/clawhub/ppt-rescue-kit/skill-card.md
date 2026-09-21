## Description:

Create or finish an editable PowerPoint for work updates, proposals, or talks, with speaker notes and sources retained in JishuDB. / 制作或补完工作汇报、提案和分享PPT，交付可编辑文件、讲稿和来源，并保存到JishuDB。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and presentation authors use this skill to create or rescue editable PowerPoint decks for work updates, proposals, and talks. It helps gather sources, draft slide copy and speaker notes, generate the deck, and retain source and revision records in JishuDB.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow saves deck drafts, sources, citations, and revision records into a selected JishuDB knowledge base.

Mitigation: Confirm the knowledge base, retained sources, and output folder before allowing write access.

Risk: Generated presentations can contain unsupported claims, invented chart data, or layout issues if source review and deck inspection are skipped.

Mitigation: Use approved sources, mark unsupported claims, inspect the generated deck for editability and overflow, and disclose inspection limitations.

Risk: A missing JishuDB connection, write privilege, or editable PowerPoint generator prevents the skill from producing its promised deliverable.

Mitigation: Verify live host capabilities and required approvals before generation, and report BLOCKED instead of substituting an outline for a finished deck.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/ppt-rescue-kit)
- [Project homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/ppt-rescue-kit)

## Skill Output:

**Output Type(s):** [files, markdown, text, guidance]

**Output Format:** [Editable PPTX plus Markdown companion files and concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected artifacts include presentation.pptx, slides.md, sources.md, and revision.md when host capabilities and approvals are available.]

## Skill Version(s):

0.1.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
