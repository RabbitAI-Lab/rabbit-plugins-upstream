## Description: <br>
RSS AI Reader helps agents set up RSS/Atom feed monitoring that summarizes articles with Claude or OpenAI and sends Chinese summaries to Feishu, Telegram, or email. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benzema216](https://clawhub.ai/user/benzema216) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to configure scheduled RSS/Atom monitoring, generate LLM summaries, deduplicate articles with SQLite, and push concise updates to team or personal notification channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses LLM API keys, notification webhooks, bot tokens, and email credentials that could expose accounts or channels if mishandled. <br>
Mitigation: Store secrets in environment variables or a vault and use least-privilege credentials for notification services. <br>
Risk: Feed content may be sent to selected AI providers and notification channels. <br>
Mitigation: Only process feeds whose content is appropriate to share with the configured AI and delivery services. <br>
Risk: The quick start installs code from a referenced GitHub repository. <br>
Mitigation: Review the repository and requirements before installation, prefer a pinned commit for repeat use, and test with --once before scheduled execution. <br>


## Reference(s): <br>
- [Configuration Guide](references/config_guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/benzema216/skills/rss-ai-reader) <br>
- [Referenced GitHub Repository](https://github.com/BENZEMA216/rss-reader.git) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference API keys, webhook URLs, bot tokens, SMTP credentials, RSS feed URLs, scheduling intervals, and SQLite database paths supplied by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
