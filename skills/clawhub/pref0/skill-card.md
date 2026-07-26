## Description: <br>
Learn user preferences from conversations and personalize responses automatically. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fliellerjulian](https://clawhub.ai/user/fliellerjulian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to track conversation-derived preferences, retrieve a user's learned profile before responding, and delete stored preferences when a reset or removal is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends whole chats and stable user identifiers to a third-party preference service. <br>
Mitigation: Use opaque internal user IDs, avoid tracking sensitive conversations, and install only when pref0 data retention is acceptable. <br>
Risk: The returned profile includes a prompt that could influence future agent behavior. <br>
Mitigation: Prefer structured preferences over directly injecting the returned prompt, and review how preferences are applied before use. <br>
Risk: Stored preferences may need to be reset or removed for a user. <br>
Mitigation: Use the documented delete endpoint when a user requests preference reset or data removal. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fliellerjulian/skills/pref0) <br>
- [pref0 API](https://api.pref0.com) <br>
- [pref0 signup](https://pref0.com/signup) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PREF0_API_KEY and a stable user identifier.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; SKILL.md frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
