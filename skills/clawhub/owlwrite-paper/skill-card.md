## Description:

End-to-end paper workbench for literature search, drafting, school-template typesetting, similarity and AI-content checks, and citation verification through OwlWrite MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and students use this skill to find literature, draft and format papers, create research figures, and request similarity, AI-content, formatting, and citation checks. It connects these workflows to the OwlWrite service and can upload manuscript files for supported tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rated the release suspicious with medium confidence and cited credential handling, manuscript uploads, paid actions, and promotional features; scan coverage was partial.

Mitigation: Review the skill before installation. Keep the API key in local configuration, disclose remote manuscript processing before uploading, and use current quotes with explicit user confirmation before paid work. Avoid promotional or reward actions unless the user requests them and their terms are explained.

Risk: Manuscripts and other user files may contain sensitive or unpublished material and are uploaded for supported remote checks and formatting.

Mitigation: Explain the upload before proceeding, confirm the user is authorized to share the file, and avoid uploading material the user does not want processed by the service.

Risk: Writing, full-text retrieval, formatting, figures, and checks can consume paid credits.

Mitigation: Show the current quote and credit cost, then get the user's confirmation before each paid action.

Risk: The configured API key can access the user's account and credits if exposed.

Mitigation: Keep the key in the user's local MCP configuration and never paste or share it; revoke and replace it if exposure is suspected.

## Reference(s):

- [ClawHub release](https://clawhub.ai/j-levee/skills/owlwrite-paper)
- [OwlWrite website and account services](https://paper.skillsutra.cn)
- [OwlWrite pricing](https://paper.skillsutra.cn/price)
- [OwlWrite service endpoint](https://owl.skillsutra.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, PDF, Word documents, Figures, Reports]

**Output Format:** [Markdown and structured text in chat; downloadable PDF, DOCX, figure, and report files where supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include literature records, reference lists, formatted manuscripts, research figures, and service reports. Applicable workflows send manuscript files to the OwlWrite service.]

## Skill Version(s):

1.2.3 (source: frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
