## Description: <br>
Command-line tool to manage Wiki.js content, pages, assets, templates, and backups via its GraphQL API with search, update, sync, and analysis functions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hopyky](https://clawhub.ai/user/hopyky) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, documentation maintainers, and agent operators use this skill to administer Wiki.js pages, assets, templates, backups, and content-quality checks through a configured CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Wiki.js API token stored in ~/.config/wikijs.json. <br>
Mitigation: Use a least-privilege token and protect the local configuration file. <br>
Risk: The CLI can perform destructive or broad changes such as delete, restore, bulk update, and search-and-replace operations. <br>
Mitigation: Review proposed destructive and bulk actions before approval, and use dry-run or confirmation flows where available. <br>
Risk: API traffic can expose administration activity or credentials if sent over an insecure connection. <br>
Mitigation: Configure the Wiki.js URL with HTTPS whenever possible. <br>
Risk: Asset upload commands can publish local files to Wiki.js. <br>
Mitigation: Upload only files that are intentionally selected and approved for publication. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hopyky/skills/wikijs) <br>
- [Wiki.js](https://js.wiki/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI output in table, JSON, or markdown formats.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can read, write, delete, upload, back up, restore, sync, and analyze Wiki.js content through a configured GraphQL API token.] <br>

## Skill Version(s): <br>
1.4.0 (source: evidence release, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
