## Description:

Translate Chinese patent applications, priority texts, claims, descriptions, abstracts, drawing text, sequence-listing references, or invention disclosures into filing-support drafts for Europe, the United States, Japan, or Korea while preserving source support, claim scope, terminology, and destination-specific patent style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External patent teams, translators, and IP practitioners use this skill to turn authoritative Chinese patent source material into EP, US, JP, or KR filing-support translations with terminology, ambiguity, change, and QA records. The output is a drafting aid that requires qualified destination counsel and, where appropriate, translator review before filing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential unpublished patent material could be exposed if sent to an unapproved external connector.

Mitigation: Use PatSnap connectors only for approved published or non-confidential material, and follow the user's confidentiality and file-handling constraints.

Risk: A filing-support translation could be mistaken for a certified translation, legal opinion, or filing-ready instruction.

Mitigation: Label outputs as drafting aids and require qualified destination counsel and, where appropriate, a competent patent translator to review support, scope, formal requirements, and deadlines.

Risk: Incomplete, ambiguous, OCR-derived, or conflicting source material can alter claim scope or introduce unsupported matter.

Mitigation: Inventory source revisions, disclose missing or unreadable material, preserve locators, keep ambiguity/change registers, and avoid inventing absent content.

## Reference(s):

- [European Patent Translation Reference](references/europe.md)
- [United States Patent Translation Reference](references/united-states.md)
- [Japan Patent Translation Reference](references/japan.md)
- [Korea Patent Translation Reference](references/korea.md)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with structured filing-support translation sections, terminology registers, ambiguity/change registers, and QA notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include destination-specific folder or file structure when requested; drafts require counsel and translator review before filing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
