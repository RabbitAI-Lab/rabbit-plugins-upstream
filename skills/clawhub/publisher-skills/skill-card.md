## Description: <br>
Publish HTML frontend projects to the PushWebly publishing platform, list published projects, obtain shareable project URLs, change a published app's public/private visibility, and package published HTML projects into Android APKs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[publisher-skill](https://clawhub.ai/user/publisher-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to publish local zipped HTML frontend projects to PushWebly, manage published project visibility, retrieve shareable URLs, and request Android APK packaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local account passwords may be persisted in plaintext. <br>
Mitigation: Prefer a temporary token when possible, restrict local credential file permissions, and remove ~/.publisher/config.json when the skill is no longer needed. <br>
Risk: Published project visibility could be broader than intended. <br>
Mitigation: Confirm public or private visibility explicitly before publishing or changing visibility, and verify the final URL and access password returned by the platform. <br>
Risk: Project zip contents are uploaded to PushWebly for hosting and optional APK packaging. <br>
Mitigation: Review the zip contents before upload and avoid publishing secrets, private data, or files that should not be sent to the platform. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/publisher-skill/ai-game-publisher) <br>
- [ClawHub skill page](https://clawhub.ai/publisher-skill/skills/publisher-skills) <br>
- [PushWebly platform](https://pushwebly.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce publishing URLs, APK download URLs, project visibility status, and credential-handling instructions.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
