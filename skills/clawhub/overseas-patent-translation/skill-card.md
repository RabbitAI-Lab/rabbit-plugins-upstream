## Description:

Translates Chinese patent application materials into jurisdiction-specific filing text for Europe, the United States, Japan, and Korea while preserving terminology, claim scope, and formatting requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent teams, translators, and agents use this skill to translate Chinese patent application content into EP, US, JP, or KR filing-oriented text. It helps preserve source disclosure, claim numbering, terminology consistency, jurisdiction-specific section order, and translation QA notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpublished or confidential patent drafts may be exposed to external lookup tools if broad MCP services are enabled during translation work.

Mitigation: Enable only the PatSnap MCP services needed for the task, avoid sending source invention details to external tools unless explicitly intended, and prefer explicit invocation for sensitive patent translation.

Risk: Patent translation can accidentally add unsupported technical features, narrow claim scope, or alter claim relationships.

Mitigation: Review translated claims against the Chinese source text, verify numbering and dependencies, and check terminology, units, formulas, figure references, and jurisdiction-specific formatting before filing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/overseas-patent-translation)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [PatSnap MCP marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [Europe patent translation reference](artifact/references/europe.md)
- [United States patent translation reference](artifact/references/united-states.md)
- [Japan patent translation reference](artifact/references/japan.md)
- [Korea patent translation reference](artifact/references/korea.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown patent translation output with jurisdiction sections, terminology glossary, and translation QA notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports Europe, United States, Japan, and Korea filing formats; depends on user-provided Chinese patent materials and optional PatSnap MCP configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
