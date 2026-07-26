## Description: <br>
Publishes HTML frontend projects to PushWebly, manages published project visibility and listings, and can package published HTML projects as Android APKs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[publisher-skill](https://clawhub.ai/user/publisher-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to publish local HTML frontend zip projects to PushWebly, obtain shareable links, manage public or private access, list published projects, and generate Android APK packages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing project zip files can expose secrets or private data to PushWebly or to public links. <br>
Mitigation: Remove secrets and private data from project zips before publishing, and explicitly choose public or private visibility. <br>
Risk: Reusable login credentials may be stored locally in ~/.publisher/config.json. <br>
Mitigation: Avoid storing long-lived credentials unless the user accepts that risk, and review or delete ~/.publisher/config.json after use. <br>
Risk: Published projects can be made publicly accessible by link. <br>
Mitigation: Confirm visibility before publishing and use private access with a separate password when public access is not intended. <br>


## Reference(s): <br>
- [ClawHub Publisher skill page](https://clawhub.ai/publisher-skill/skills/publisher-2) <br>
- [Server-resolved source repository](https://github.com/publisher-skill/publisher) <br>
- [PushWebly platform](https://pushwebly.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON snippets, and API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include project URLs, visibility status, access-password handling guidance, project identifiers, and APK download URLs.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
