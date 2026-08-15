## Description:

Create an evidence-bounded English patent-based R&D briefing from an authorized Excel workbook. Use when a user supplies patent records and asks to screen relevance, organize reviewed records by technology route and organization, preserve approved workbook links or figures, and generate a self-contained scientific HTML briefing with reproducible scope, review provenance, and patent-professional boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and R&D teams use this skill to turn authorized patent workbook exports into evidence-bounded technology briefings. It supports relevance screening, reviewed category organization, workbook-link and figure preservation, and static HTML reporting with clear patent-professional boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent workbooks, embedded figures, and links may contain confidential or rights-restricted material.

Mitigation: Process only authorized local workbooks, confirm rights for embedded figures and links, and apply the intended confidentiality and distribution restrictions before release.

Risk: A generated briefing could be mistaken for legal advice, patent clearance, or exhaustive global coverage.

Mitigation: Require human review of included records, disclose scope and evidence cutoffs, and obtain patent-professional review for material claim, status, FTO, validity, enforceability, or infringement questions.

Risk: Untrusted dependencies or topic configuration files could affect local processing behavior.

Mitigation: Install only into a chosen directory, review requirements before dependency installation, and use trusted topic configuration files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/create-patent-based-rd-briefing-rd)
- [PatSnap Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands; generated workbook and self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized local Excel workbook, trusted topic configuration, human review, and patent-professional review for material legal questions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
