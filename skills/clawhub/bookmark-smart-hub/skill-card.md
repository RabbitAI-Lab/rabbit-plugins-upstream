## Description: <br>
Bookmark Smart Hub helps agents monitor bookmarks, extract and analyze saved content with AI, send notifications, and search a local knowledge base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Knowledge workers, researchers, teams, and developers use this skill to automate bookmark monitoring, content extraction, AI analysis, knowledge-base search, trend discovery, notification routing, and data export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session-style social credentials and notification tokens may expose accounts or channels if copied into chats, repos, logs, or broad configuration files. <br>
Mitigation: Use scoped official API credentials where possible, restrict permissions, store secrets only in local ignored files, and rotate any token that may have been exposed. <br>
Risk: The background daemon can continuously monitor bookmarks and send content to external AI or notification providers. <br>
Mitigation: Start the daemon only after reviewing what will be monitored, which providers will receive content, and which notification channels are enabled. <br>
Risk: AI analysis of saved pages can produce incomplete or misleading summaries, priorities, or project recommendations. <br>
Mitigation: Review generated analysis before acting on it, especially for business, security, legal, financial, or operational decisions. <br>


## Reference(s): <br>
- [Skill homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bookmark-smart-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON examples, shell command snippets, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require local files, API credentials, Node.js v16+, PM2, and external AI or notification provider access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
