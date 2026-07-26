## Description: <br>
Run Clawbridge discovery from OpenClaw chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leethebuilder](https://clawhub.ai/user/leethebuilder) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw users use this optional chat shortcut to run the external Clawbridge CLI, receive a candidate count, and open the Clawbridge Vault review link. It is intended for users who already trust and operate a Clawbridge workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs an external Clawbridge CLI and depends on trust in the Clawbridge cloud service. <br>
Mitigation: Install and use it only when the Clawbridge service, CLI, and workspace are trusted for the intended data. <br>
Risk: Discovery results may be uploaded to Clawbridge Vault, creating data-sharing and retention considerations. <br>
Mitigation: Use scoped workspaces or profiles and avoid sensitive material unless the Vault upload and retention practices are acceptable. <br>
Risk: The documented installer is a remote shell script. <br>
Mitigation: Review the installer before running it when possible and install in an environment appropriate for the data being processed. <br>


## Reference(s): <br>
- [Clawbridge homepage](https://clawbridge.cloud) <br>
- [Clawbridge install script](https://clawbridge.cloud/install) <br>
- [ClawHub skill page](https://clawhub.ai/leethebuilder/skills/clawbridge-skill-latest) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown-style chat response with parsed CLI output and a Vault URL] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs the local clawbridge command, parses VAULT_URL and CANDIDATES_COUNT from stdout, and returns a concise review link response.] <br>

## Skill Version(s): <br>
3.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
