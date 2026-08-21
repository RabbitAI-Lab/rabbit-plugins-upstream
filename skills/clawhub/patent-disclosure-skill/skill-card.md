## Description:

中国专利技能：专利点挖掘与交底书（发明/实用/外观）编写，通俗解读专利，嗅探政策动向，辅助审查答复。| China patents skill: mine patent points and draft disclosures (invention / utility model / design), plain-language reading, policy sniffing, assisted office-action response.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, inventors, patent practitioners, and technically oriented teams use this skill to mine Chinese patent points, draft invention, utility model, or design disclosures, read published patents in plain language, monitor patent policy signals, and prepare office-action response drafts for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes private patent, project, office-action, and document materials, and evidence.security marks the release suspicious because of risky dependency versions and weaker API-key handling.

Mitigation: Install in an isolated environment, pin or upgrade document and SVG dependencies before processing untrusted files, avoid putting secrets in chat or command-line flags, and prefer environment variables for embedding credentials.

Risk: Vault writes, generated diagrams, STEP/CAD handling, and document conversion can modify or create files in user workspaces.

Mitigation: Back up Obsidian vaults and project folders before enabling vault writes or STEP/CAD processing, and review generated drafts and file outputs before using them in patent workflows.

Risk: Patent disclosure drafts, prior-art notes, and office-action responses may contain incomplete, incorrect, or legally consequential guidance.

Mitigation: Treat outputs as drafts for qualified human review, especially before filing, submitting office-action responses, or relying on policy and prior-art findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill)
- [SKILL.md](SKILL.md)
- [Installation guide](INSTALL.md)
- [Patent Obsidian format](references/patent_obsidian_format.md)
- [Patent domain rules](references/patent_domain_rules.yaml)
- [Patent type search mapping](references/patent_type_search.yaml)
- [Obsidian setup guide](docs/obsidian-setup-guide.md)
- [CNIPA patent publication search](http://epub.cnipa.gov.cn/)
- [Obsidian CLI documentation](https://help.obsidian.md/cli)
- [Playwright documentation](https://playwright.dev/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown and structured files with optional shell commands and generated document assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce patent disclosure drafts, plain-language patent notes, Obsidian vault material, office-action response drafts, diagrams, DOCX files, and review checklists depending on the selected mode.]

## Skill Version(s):

3.6.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
