## Description: <br>
Audits a page's on-page SEO signals and returns scored findings with prioritized repair recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing practitioners, SEO specialists, and developers use this skill to audit user-provided URLs or page content for title tags, metadata, heading structure, keyword usage, links, images, schema, and prioritized fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may direct use of connected SEO accounts, crawlers, or local helper execution beyond a narrow page audit. <br>
Mitigation: Keep audits to user-provided pages or clearly approved URLs, and enable connected accounts or local helpers only after explicit trust and scope decisions. <br>
Risk: Bulk audits and keyword recommendations may rely on samples or estimates when complete SEO data is unavailable. <br>
Mitigation: Require reports to label measured, user-provided, and estimated data, and confirm target keywords or data gaps before acting on recommendations. <br>
Risk: CORE-EEAT quick-scan findings may be mistaken for a full publish-readiness judgment. <br>
Mitigation: Treat CORE-EEAT output as a referral signal and use a dedicated content-quality review for publication decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/on-page-seo-checker) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Scoring Rubric](references/scoring-rubric.md) <br>
- [Audit Templates](references/audit-templates.md) <br>
- [Bulk Audit Playbook](references/bulk-audit-playbook.md) <br>
- [Audit Example and Checklists](references/audit-example.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit report with score tables, prioritized fix lists, and a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should label metrics as measured, user-provided, or estimated, and mark unavailable data as N/A.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
