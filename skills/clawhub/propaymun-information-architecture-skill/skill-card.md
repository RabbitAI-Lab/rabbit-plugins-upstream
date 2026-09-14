## Description:

Shape, review, and validate end-to-end product information architecture, product/UX sitemaps, and stateful user flows when users need clearer structure, labels, relationships, access, findability, destinations, or task paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kamroncorp](https://clawhub.ai/user/kamroncorp)

### License/Terms of Use:

MIT-0

## Use Case:

External product teams, designers, researchers, content strategists, and developers use this skill to turn product context into evidence-aware information architecture, product sitemaps, stateful user flows, validation checks, and downstream handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence product-structure recommendations in any workspace where it is installed.

Mitigation: Install it only in workspaces where IA guidance is intended to affect responses.

Risk: Optional Python helpers read and may write explicit local file paths.

Mitigation: Run helpers only on files you choose, use fresh output paths, and rely on the host's normal permission controls.

Risk: Builder handoffs can contain source-derived product content that downstream tools may interpret imperfectly.

Mitigation: Review unfamiliar source material before giving generated handoffs to tools with file, network, or private-data access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kamroncorp/skills/propaymun-information-architecture-skill)
- [README](README.md)
- [Security Scope](SECURITY.md)
- [IA Foundations and Decision Rules](references/ia-foundations.md)
- [Modeling and Option Generation](references/modeling.md)
- [Product and UX Sitemap](references/sitemap.md)
- [Stateful User Flow](references/user-flow.md)
- [IA Validation and Measurement](references/validation.md)
- [Visual Builder Handoff](references/visual-builder-handoff.md)
- [Semantic IA Schema](schema/semantic-ia.schema.json)
- [Product Sitemap Schema](schema/product-sitemap.schema.json)
- [User Flow Schema](schema/user-flow.schema.json)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, JSON, code, shell commands, configuration]

**Output Format:** [Conversational guidance, Markdown handoffs, structured JSON models, optional code or shell commands, and configuration instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local helpers operate only on explicit file paths chosen by the user and do not require network access or credentials.]

## Skill Version(s):

1.0.1 (source: metadata, VERSION, and changelog, released 2026-09-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
