## Description: <br>
Collects and summarizes Korean security news hourly from 11 sources using Gemini API, then publishes to Notion and optionally to Tistory blog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rebugui](https://clawhub.ai/user/rebugui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security analysts, operators, and developers use this skill to monitor Korean security sources, generate concise summaries, and publish curated updates to Notion or Tistory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically change external Notion data and publish content with limited user control. <br>
Mitigation: Use a dedicated Notion database, restrict API tokens to the minimum required access, and review generated content before enabling publication workflows. <br>
Risk: Optional Tistory publishing can post generated content to a public blog. <br>
Mitigation: Keep Tistory publishing disabled unless explicitly needed and use a separate publishing account or draft workflow for review. <br>
Risk: The automatic 90-day Notion archive cleanup can archive data that should be retained. <br>
Mitigation: Disable or patch the cleanup behavior and test it against a dedicated database before running the skill on real data. <br>
Risk: Configured Notion, Slack, Tistory, or Chrome profile data may be sensitive or business-critical. <br>
Mitigation: Use isolated accounts or profiles, store credentials securely, and avoid granting broad access to production workspaces. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/rebugui/security-news-feed-repo) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Gemini API key setup](https://aistudio.google.com/apikey) <br>
- [Notion integration setup](https://www.notion.so/my-integrations) <br>
- [Tistory API guide](https://www.tistory.com/guide/api/manage) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown summaries, Notion pages, optional Tistory posts, and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured API credentials for Gemini, Notion, and optional Tistory publishing.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
