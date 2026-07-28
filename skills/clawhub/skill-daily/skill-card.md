## Description: <br>
Clawhub Daily fetches ClawHub skill listings, ranks daily recommendations across multiple dimensions, and produces local or optionally delivered briefings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, team leads, content creators, and ClawHub users can use this skill to receive recurring recommendations about useful or trending AI agent skills. It is suited for scheduled daily or every-other-day briefings and for manual discovery sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommendation briefings may be sent to Feishu or IMA when credentials are configured. <br>
Mitigation: Review configured delivery credentials before scheduled runs, and use --skip-push for local-only operation. <br>
Risk: Real Feishu or IMA credentials could be exposed if placed in published configuration files. <br>
Mitigation: Keep real credentials out of published files and prefer environment variables or local-only configuration. <br>
Risk: IMA delivery may target an unintended knowledge base if the target is left implicit. <br>
Mitigation: Set an explicit IMA knowledge-base ID before enabling IMA delivery. <br>
Risk: The skill writes local snapshots, recommendation reports, and optional Obsidian copies. <br>
Mitigation: Review configured filesystem paths such as data/snapshots, data/recommended, the Obsidian inbox, and the saved fallback before recurring use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardwason/skills/skill-daily) <br>
- [Setup Wizard](references/setup-wizard.md) <br>
- [Cron Prompt Templates](references/prompt-templates.md) <br>
- [API Contract](references/api-contract.md) <br>
- [Briefing Template](references/briefing-template.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON reports, plus optional delivery to Feishu, IMA, or Obsidian when configured.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local snapshots and recommendation reports; external delivery occurs only when the corresponding credentials are configured.] <br>

## Skill Version(s): <br>
2.0.8 (source: release evidence, SKILL.md frontmatter, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
