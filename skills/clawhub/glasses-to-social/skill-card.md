## Description: <br>
Glasses to Social monitors a Google Drive folder for smart-glasses images, uses vision AI to draft social posts in the user's voice, and keeps publishing behind user approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[junebugg1214](https://clawhub.ai/user/junebugg1214) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External creators and developers use this skill to set up a hands-free workflow that turns smart-glasses photos into reviewable social media drafts. The skill is intended for photo monitoring, image analysis, caption drafting, and approval-gated publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A link-viewable Google Drive folder can expose sensitive smart-glasses photos. <br>
Mitigation: Use a dedicated folder containing only photos intended for processing, keep sharing as narrow as possible, and avoid placing private or workplace images in the watched folder. <br>
Risk: Generated social posts may reveal faces, minors, screens, IDs, documents, or location details from incoming photos. <br>
Mitigation: Manually review every image preview and caption before publishing; keep approval-gated posting enabled. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/junebugg1214/skills/glasses-to-social) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local downloaded image files and update a processed-photo JSON file when scripts are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
