## Description: <br>
Upload local files or directories to PinMe public IPFS and return short shareable pinit.eth.limo URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to publish selected local files, directories, or generated HTML to PinMe public IPFS and return a shareable URL. It also supports AppKey setup, upload history, unpinning, wallet checks, logout, and structured error handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected local files or directories can be uploaded to public IPFS and may remain accessible after unpinning. <br>
Mitigation: Confirm each upload target, avoid private or credential-bearing files, and keep the upload warning enabled except in reviewed automation. <br>
Risk: The skill stores a PinMe AppKey locally for reuse. <br>
Mitigation: Use PINME_APPKEY for one-shot runs when persistence is not desired, protect the configured key file, and run logout when the key should be removed. <br>
Risk: The script can install the PinMe npm CLI at runtime if it is missing. <br>
Mitigation: Preinstall and review or pin the PinMe CLI in managed environments before using the skill. <br>


## Reference(s): <br>
- [ClawHub Pinme Share page](https://clawhub.ai/songhonglei/skills/pinme-share) <br>
- [PinMe service](https://pinme.eth.limo) <br>
- [Skill documentation](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and final-line JSON results from the upload script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uploads selected paths to public IPFS, returns shareable URLs, and reports structured error_type values for agent routing.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
