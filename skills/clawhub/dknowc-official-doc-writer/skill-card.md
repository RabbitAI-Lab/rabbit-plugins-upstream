## Description:

深知公文写作 helps users draft, rewrite, polish, review, and package formal Chinese workplace documents, including official documents, reports, letters, meeting minutes, summaries, plans, speeches, research reports, Word documents, and optional red-head document formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, office staff, administrative teams, secretarial roles, and enterprise or public-sector users use this skill to turn notes, meeting records, research material, drafts, and instructions into structured formal Chinese documents. It can also retrieve source material through DKnowC search when policy evidence, data, standards, or case references are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search or outline prompts may be sent to DKnowC when the user asks for policy evidence, data, standards, or reference cases.

Mitigation: Use the search features only when needed, avoid sending sensitive material in prompts, and review the generated source-reference report before relying on the output.

Risk: The skill can guide phone verification and store a DKNOWC_API_KEY value in ~/.zshrc.

Mitigation: Prefer a secure secret store or the provider website in sensitive environments, do not expose full API keys in chat, and review shell profile changes before reuse.

Risk: Generated formal documents may contain incorrect wording, policy interpretation, or unsupported claims.

Mitigation: Review the document, source references, and formatting before submission or publication, especially for official, legal, financial, or policy-sensitive uses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer)
- [README](artifact/README.md)
- [Task router](artifact/reference/task_router.md)
- [Search policy](artifact/reference/search_policy.md)
- [Material usage guidance](artifact/reference/material_usage_guidance.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [Document standards index](artifact/reference/standards/00_索引.md)
- [DKnowC open platform](https://open.dknowc.cn/)
- [DKnowC management platform](https://platform.dknowc.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, generated text, shell commands, configuration steps, .docx files, and HTML source-reference reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create Word documents, optional red-head Word documents, local initialization state, search result intermediates, and HTML provenance reports; PDF generation is not supported by the artifact.]

## Skill Version(s):

3.3.1 (source: server evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
