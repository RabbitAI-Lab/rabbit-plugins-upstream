## Description: <br>
Uploads local BIM, CAD, and 3D model files to BIMWing for online lightweight conversion, then returns browser-viewable share links and supports model listing, conversion status checks, and share-link creation for existing models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolboy-never-die](https://clawhub.ai/user/coolboy-never-die) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and BIM/CAD practitioners use this skill to upload selected model or drawing files to BIMWing, wait for conversion, and receive a share link for browser-based viewing. Users can also query their BIMWing account for model lists, conversion status, and share links for existing models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected BIM/CAD files are sent to BIMWing for conversion. <br>
Mitigation: Confirm the exact local file path and sharing intent before upload. <br>
Risk: Generated BIMWing share links may be viewable without login. <br>
Mitigation: Share only intended links and avoid uploading sensitive models unless public-link access is acceptable. <br>
Risk: BIMWing credentials can be saved as plaintext in config.local.json. <br>
Mitigation: Prefer environment variables when possible; save credentials only after explicit consent and avoid saved credentials on shared machines. <br>
Risk: Account-level list, status, and share operations can access model information in the user's BIMWing account. <br>
Mitigation: Run account-level operations only when the user explicitly asks for them. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/coolboy-never-die/skills/bimwing-convert) <br>
- [BIMWing web application](https://bimwing.letsgrp.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown or terminal text containing model status, share URLs, and local HTML open-page file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a local HTML open page for a generated BIMWing share link.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
