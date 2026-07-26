## Description: <br>
Bookmark Intelligence monitors X bookmarks, fetches linked article text, uses AI to extract summaries, key concepts, action items, and project-specific recommendations, and can send high-value insights to Telegram. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, researchers, and content workers use this skill to turn X bookmarks and linked articles into structured summaries, action items, project matches, local JSON knowledge records, and optional Telegram notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup asks for X session cookies, which can grant local automation access to the user's X account. <br>
Mitigation: Use a dedicated low-risk X account where possible, protect the .env file, and rotate or revoke the X session if the machine or project directory is exposed. <br>
Risk: The PM2 background poller can continue processing bookmarks when the user is not actively supervising it. <br>
Mitigation: Run the daemon only when needed, review PM2 status and logs, and disable or stop the daemon between monitoring periods. <br>
Risk: Bookmark content and linked-article text may be sent to AI providers for analysis. <br>
Mitigation: Avoid processing sensitive bookmarks unless the selected AI provider and account settings are appropriate for that data. <br>
Risk: Analysis files are stored locally and may include tweet content, article content, project context, and generated recommendations. <br>
Mitigation: Protect the project directory, keep generated analysis files out of version control, and remove stored records that contain sensitive material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bookmark-intelligence) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON configuration or analysis examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local bookmark analysis JSON files and may trigger Telegram notifications for high-priority insights.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
