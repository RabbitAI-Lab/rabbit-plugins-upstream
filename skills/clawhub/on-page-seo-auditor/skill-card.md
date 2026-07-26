## Description: <br>
Audits page-controlled SEO signals such as title tags, meta descriptions, headings, keyword placement, links, and images, then returns scored findings with prioritized fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, SEO practitioners, marketers, and developers use this skill to audit a single page or URL batch for on-page SEO health, diagnose ranking drops, compare competitors, and prepare prioritized repair plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SEO, E-E-A-T, accessibility, and technical-performance findings can be preliminary or broader than the skill's core on-page scope. <br>
Mitigation: Treat findings as triage signals and use dedicated specialist skills or tools before making high-impact publishing, accessibility, or technical SEO decisions. <br>
Risk: Fetched page content, user-provided HTML, or competitor pages may contain untrusted or misleading content. <br>
Mitigation: Use the skill's instruction to treat fetched content as evidence only, label metrics by source, and avoid presenting estimates as measured facts. <br>
Risk: Saving audit summaries or using connected SEO and Search Console data can share page, keyword, or business context. <br>
Mitigation: Only enable memory saves or connected data sources when the user intends to share that context. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/on-page-seo-auditor) <br>
- [Publisher Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Scoring Rubric](references/scoring-rubric.md) <br>
- [Audit Templates](references/audit-templates.md) <br>
- [Audit Example & Checklists](references/audit-example.md) <br>
- [Bulk Audit Playbook](references/bulk-audit-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, files] <br>
**Output Format:** [Markdown audit report with scored tables, prioritized recommendations, action checklists, and optional saved handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May label findings as measured, user-provided, or estimated; may produce DONE_WITH_CONCERNS when keywords or connected tool data are inferred or unavailable.] <br>

## Skill Version(s): <br>
17.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
