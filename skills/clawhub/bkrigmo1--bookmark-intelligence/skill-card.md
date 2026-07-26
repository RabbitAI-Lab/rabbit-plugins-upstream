## Description: <br>
Automatically monitors X bookmarks, fetches linked articles, analyzes content with AI, and delivers project-relevant insights and notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bkrigmo1](https://clawhub.ai/user/bkrigmo1) <br>

### License/Terms of Use: <br>
Proprietary - Licensed per user <br>


## Use Case: <br>
External users and developers use this skill to turn X bookmarks and linked articles into project-aware summaries, actionable items, local knowledge-base records, and optional notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires X auth_token and ct0 cookies that provide effective full-session access to the user's X account. <br>
Mitigation: Use a low-value or dedicated X account where possible, keep the .env file out of backups and repositories, and rotate cookies if exposure is suspected. <br>
Risk: Automated monitoring can continuously process bookmarks and fetch arbitrary linked pages. <br>
Mitigation: Run manually or with a conservative schedule until reviewed, and disable daemon mode or automatic link fetching unless it is needed. <br>
Risk: Bookmark-derived content may be sent through external LLM analysis or notification paths when enabled. <br>
Mitigation: Review configuration before enabling LLM analysis or notifications, and avoid sending sensitive bookmarks to external services. <br>
Risk: Payment and licensing flows are included in the release. <br>
Mitigation: Avoid payment and licensing commands unless they are explicitly needed and configured for the intended deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bkrigmo1/skills/bookmark-intelligence) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Sample analysis output](artifact/examples/sample-analysis.json) <br>
- [bird CLI](https://github.com/yardencsGitHub/bird) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON analysis records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores bookmark analyses locally and can emit notifications when enabled.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
