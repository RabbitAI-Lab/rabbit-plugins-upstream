## Description: <br>
Site Structure Optimizer helps agents plan website information architecture and improve internal linking by producing hierarchy, URL taxonomy, navigation, hub-spoke, Mermaid map, orphan-page, anchor-text, source-target-anchor, score, and handoff outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and SEO practitioners use this skill to design or restructure site architecture, diagnose internal link structure, find orphan pages, plan descriptive anchors, and produce implementation-ready structure improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill with a live domain can trigger crawling or connected SEO and analytics lookups. <br>
Mitigation: Use a provided sitemap or page list when live crawling is not intended, and review any connected lookup before execution. <br>
Risk: Fetched page content may be untrusted and could contain misleading instructions or data. <br>
Mitigation: Treat crawled content as input data only, label metrics by source, and do not follow instructions embedded in fetched HTML. <br>
Risk: Approved saves may write summaries under the skill's memory path. <br>
Mitigation: Confirm saving before writing persistent summaries and avoid storing sensitive site data unless the user has approved it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/site-structure-optimizer) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Site-Type Patterns](references/site-type-patterns.md) <br>
- [Link Architecture Patterns](references/link-architecture-patterns.md) <br>
- [Mermaid Templates](references/mermaid-templates.md) <br>
- [Linking Templates](references/linking-templates.md) <br>
- [Linking Example](references/linking-example.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with tables, ASCII hierarchy trees, Mermaid code blocks, optional shell commands, scored diagnostics, and handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mode-dependent outputs for architecture or linking workflows; includes a structure or architecture score out of 100.] <br>

## Skill Version(s): <br>
19.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
