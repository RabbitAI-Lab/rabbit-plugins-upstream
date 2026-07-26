## Description: <br>
LinkedIn inbox management with scheduled scanning, auto-draft responses following the user's communication style, and approval workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dylanbaker24](https://clawhub.ai/user/dylanbaker24) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and agents use this skill to monitor a logged-in LinkedIn inbox, summarize unread messages, draft style-matched replies, and send approved responses through browser automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect private LinkedIn messages, save screenshots, and post message details to notifications. <br>
Mitigation: Use a dedicated Chrome profile, keep unrelated sensitive tabs closed, keep notification channels private, and periodically delete /tmp LinkedIn screenshots and memory logs containing message content. <br>
Risk: The skill can send messages from a logged-in LinkedIn account through broad browser automation. <br>
Mitigation: Review the recipient and message content before every send, require explicit approval, avoid send all, and keep the configured action rate limit. <br>


## Reference(s): <br>
- [Communication Style Extraction Guide](references/style-extraction.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dylanbaker24/skills/linkedin-inbox) <br>
- [Publisher Profile](https://clawhub.ai/user/dylanbaker24) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown notifications and draft text with JSON configuration and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human approval before sending messages; may create screenshot and JSON files under /tmp.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
