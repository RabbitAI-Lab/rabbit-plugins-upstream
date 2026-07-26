## Description: <br>
Control LG smart appliances via ThinQ API. Use when user asks about their fridge, washer, dryer, AC, or other LG appliances. Supports checking status, changing temperature, toggling modes (express, eco), and monitoring door status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kaiofreitas](https://clawhub.ai/user/kaiofreitas) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to inspect and control LG ThinQ smart appliances, including refrigerators, washers, dryers, and air conditioners. It supports status checks and selected appliance controls after the user configures a ThinQ personal access token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real LG ThinQ appliances and includes a raw command path for arbitrary device-control payloads. <br>
Mitigation: Install only from a trusted publisher, review the target device and JSON payload before using raw commands, and prefer the documented bounded commands for normal appliance control. <br>
Risk: The skill depends on a local ThinQ personal access token stored in the user's home configuration directory. <br>
Mitigation: Protect the token file, avoid sharing logs or shell history that reveal token setup details, and rotate the token if it may have been exposed. <br>
Risk: The skill requires the external thinqconnect dependency to access ThinQ APIs. <br>
Mitigation: Verify the dependency source and installed package before use. <br>


## Reference(s): <br>
- [LG ThinQ Personal Access Token](https://connect-pat.lgthinq.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/kaiofreitas/skills/lg-thinq) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text CLI output and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided LG ThinQ token and country code stored in local configuration files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
