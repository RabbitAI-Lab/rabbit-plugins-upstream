## Description: <br>
Content Writer helps agents draft new SEO content and refresh decayed pages with keyword targeting, content structure, citation boundaries, CORE-EEAT checks, and republishing guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and content teams use this skill to produce SEO articles, landing pages, product copy, and refresh plans for pages with traffic or ranking decay. It is intended for agent-assisted drafting and planning before a separate quality gate reviews publish readiness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Refresh analysis may rely on estimates when analytics or ranking history is missing. <br>
Mitigation: Review metric labels and require measured or user-provided data before making publish or prioritization decisions. <br>
Risk: The skill may select a limited competitor set when several pages are available. <br>
Mitigation: Confirm the competitor set and source-backed gaps before using the refresh plan. <br>
Risk: Publishing-related index push commands can use live credentials after content is published. <br>
Mitigation: Keep dry-run behavior until a final live URL, explicit approval, and credential handling are confirmed. <br>


## Reference(s): <br>
- [Project homepage (metadata/clawdis)](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Content Decay Signals](references/content-decay-signals.md) <br>
- [Content Structure Templates](references/content-structure-templates.md) <br>
- [SEO Content Writer Detailed Instructions](references/instructions-detail.md) <br>
- [Content Refresher Worked Example and Checklist](references/refresh-example.md) <br>
- [Content Refresh Templates](references/refresh-templates.md) <br>
- [SEO Writing Checklist and Content Template](references/seo-writing-checklist.md) <br>
- [Title and Headline Formulas](references/title-formulas.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Analysis, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown content deliverables, structured analysis tables, checklist-style handoffs, and optional shell commands for gated indexing workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a dated content artifact with permission; generated metrics should be labeled Measured, User-provided, Calculated, Estimated, or Proxy.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
