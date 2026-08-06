## Description: <br>
Controls JFTech smart door lock devices by checking door-lock capability, logging in, obtaining device access tokens, reading configuration, and sending remote unlock commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage bound, online JFTech smart door locks through the JFTech OpenAPI, including capability checks, token retrieval, device login, configuration reads, and remote unlock actions. <br>

### Deployment Geography for Use: <br>
China mainland, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send a remote unlock command for a physical door without a built-in confirmation step. <br>
Mitigation: Require explicit human approval immediately before any unlock action is executed. <br>
Risk: Misconfigured endpoints or overly broad endpoint control could send requests outside documented vendor regional hosts. <br>
Mitigation: Restrict JF_ENDPOINT to documented JFTech regional API hosts. <br>
Risk: The required JF environment variables include credentials and device access tokens. <br>
Mitigation: Store credentials securely, limit access to trusted users and devices, and rotate device tokens when needed. <br>
Risk: Generic unlock triggers can cause accidental or unintended unlock requests. <br>
Mitigation: Avoid broad natural-language triggers for unlock actions and require precise operator intent. <br>


## Reference(s): <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-smart-doorlock-control) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, API Calls, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash commands and command-line text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JF account, application, device serial number, and device token environment variables.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
