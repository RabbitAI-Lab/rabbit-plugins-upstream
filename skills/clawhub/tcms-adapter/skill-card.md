## Description:

Channel-adaptation agent that adapts a reviewed core draft or published article into channel-specific publish-ready versions for WeChat, developer communities, Chinese social posts, English X posts, LinkedIn summaries, sales one-pagers, and re-promotion material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, communications, and developer-relations teams use this skill to turn already-reviewed source drafts or published articles into channel-specific marketing and social content while preserving source data, conclusions, product names, and redactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated marketing drafts may introduce inaccurate claims or alter the source draft's judgment if used without review.

Mitigation: Use only reviewed source drafts or published articles, preserve source data and conclusions, and complete the documented L1/L2 or light review before publishing.

Risk: The skill may activate on broad adaptation or rewriting requests and can write generated Markdown outputs.

Mitigation: Confirm the intended source path, target channels, and output location before use, and review generated files before they enter publishing workflows.

Risk: Customer names, sensitive details, or uncertain English phrasing could appear in adapted channel versions.

Mitigation: Carry through source redactions, auto-redact unredacted customer names when found, and route English content marked needs confirmation to human proofreading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-adapter)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown files and execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes adapted channel drafts under content/adapted/ and content/adapted/repurpose/ when used with file-writing tools.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
