## Description:

Creates and maintains Chinese knowledge bases, tutorial series, study guides, and case libraries by confirming requirements, researching sources, drafting outlines, writing articles, reviewing content, and maintaining cross-references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qingkaiwu](https://clawhub.ai/user/qingkaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and knowledge workers use this skill to turn ambiguous Chinese knowledge-base ideas, source material, and ongoing revisions into structured outlines, editable articles, project records, and maintained cross-links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated knowledge-base content may include unsupported claims, stale facts, or guidance beyond the available evidence.

Mitigation: Use the skill's source-record and review workflow, and verify high-impact or time-sensitive claims against current primary sources before publication.

Risk: The skill may read or update project records and Feishu or local documents within the requested scope.

Mitigation: Limit the document scope, require explicit authorization for external writes or sharing, and review created or updated documents before treating delivery as complete.

Risk: Reader-facing documents could accidentally expose private paths, source notes, or user-provided materials.

Mitigation: Keep private material in project records and exclude local paths or unauthorized source details from public or reader-facing outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qingkaiwu/skills/knowledge-base-editor)
- [Interview and approval](references/interview-and-approval.md)
- [Research and outline](references/research-and-outline.md)
- [Project records and citations](references/project-records.md)
- [Writing patterns](references/writing-patterns.md)
- [Review and delivery state](references/review-and-state.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Simplified Chinese Markdown or Feishu-editable document content with outlines, tables, citations, project records, and delivery notes when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is Simplified Chinese; Feishu delivery depends on available authorized tools and must be checked after writing.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter metadata says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
