## Description: <br>
cashu-emoji helps agents encode and decode Cashu token data hidden inside emojis using Unicode variation selectors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users can use this skill to transform Cashu token text into emoji-hidden text and decode it back for supported workflows. Encoded token text may represent value-bearing material and should be handled as sensitive data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hidden Cashu token data may be value-bearing and difficult to notice in normal chat or logs. <br>
Mitigation: Treat encoded and decoded token text as sensitive material; avoid pasting it into untrusted chats, logs, or shared files. <br>
Risk: The release has broad read, write, exec, and API-oriented behavior that is not clearly scoped. <br>
Mitigation: Run only in a constrained agent environment, review proposed commands before execution, and prefer a version that documents exact commands, services, and consent boundaries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cashu-emoji) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with optional JSON result examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include encoded emoji text, decoded token text, execution logs, status metadata, or configuration guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
