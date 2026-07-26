## Description: <br>
Upload image files to PixelVault and return public CDN URLs for sharing in pull requests, issues, comments, and related workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[facundofarias](https://clawhub.ai/user/facundofarias) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical contributors use this skill to upload selected screenshots, diagrams, mockups, charts, or image build artifacts and receive shareable PixelVault CDN URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive or proprietary content may be uploaded to a public, permanent, globally cached CDN URL. <br>
Mitigation: Review selected files for secrets, personal data, proprietary information, and unintended screenshots before upload. <br>
Risk: The skill depends on local PixelVault CLI configuration and authentication. <br>
Mitigation: Confirm the pixelvault CLI is installed and authenticated before upload; stop and ask the user to configure authentication if checks fail. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with one CDN URL per uploaded file; optional JSON metadata when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the pixelvault CLI and configured PixelVault authentication; returned CDN URLs are permanent and globally cached.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
