## Description: <br>
Publish HTML frontend projects to the PushWebly publishing platform, list published projects, obtain shareable project URLs, change a published app's public/private visibility, and package published HTML projects into Android APKs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[publisher-skill](https://clawhub.ai/user/publisher-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to publish local HTML frontend projects to PushWebly, manage project visibility, list published projects, and create Android APK packages from published projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish local projects to an external PushWebly service. <br>
Mitigation: Install and use it only when external publishing is intended, and confirm project visibility before each publish. <br>
Risk: Reusable PushWebly credentials may be stored in plaintext local configuration. <br>
Mitigation: Avoid saving credentials unless plaintext storage in ~/.publisher/config.json is acceptable, restrict the file to the local user, and rotate the password or token if the file is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/publisher-skill/skills/ai-game-publisher) <br>
- [Publisher profile](https://clawhub.ai/user/publisher-skill) <br>
- [Server-resolved GitHub import](https://github.com/publisher-skill/ai-game-publisher) <br>
- [PushWebly platform](https://pushwebly.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with command examples, JSON request bodies, and concise status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce shareable project URLs, private access passwords, and APK download URLs after publishing operations.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
