## Description: <br>
Searches and browses Pinterest pins, retrieves pin details, and sends actual images via messaging when a user wants inspiration, images, or ideas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xs4m1337](https://clawhub.ai/user/0xs4m1337) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search or browse Pinterest, inspect pin details, and send image results directly in chat for inspiration or visual research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Python helper can install httpx at runtime if the dependency is missing. <br>
Mitigation: Install and review dependencies deliberately in a controlled environment before running the helper. <br>
Risk: The skill can handle Pinterest access tokens, app secrets, and account content. <br>
Mitigation: Use read-only Pinterest scopes, keep tokens and secrets out of logs and prompts, and rotate credentials if exposed. <br>
Risk: The skill may retrieve or share scraped media and screenshots from Pinterest. <br>
Mitigation: Send media or screenshots only when the user clearly requested that Pinterest content and review results before sharing. <br>


## Reference(s): <br>
- [Pinterest OAuth Setup](references/oauth-setup.md) <br>
- [Pinterest API v5 Reference](references/api-reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/0xs4m1337/skills/pinterest) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with browser and messaging commands, bash examples, and optional JSON from the helper script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Pinterest image URLs, screenshots, or direct media-send instructions; the helper script can emit JSON with --json.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
