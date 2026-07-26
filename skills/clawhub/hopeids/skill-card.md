## Description: <br>
Openclaw Plugin provides inference-based intrusion detection for OpenClaw agents, including message scanning, quarantine records, and human review commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emberdesire](https://clawhub.ai/user/emberdesire) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
Developers and agent operators use this plugin to scan incoming agent messages for jailbreaks, prompt injection, credential theft, command injection, and related risks. It can warn, block, quarantine metadata, and expose review commands for approving, rejecting, or trusting senders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that the plugin may under-disclose where message content is sent for analysis. <br>
Mitigation: Disable external classifier paths unless the deployment accepts sending flagged prompt excerpts to the configured model or agent. <br>
Risk: Trusted-owner bypass can reduce scanning coverage in higher-risk deployments. <br>
Mitigation: Set trustOwners to false when owner messages should be scanned like other inputs. <br>
Risk: Telegram alert delivery may not be reliable without environment-specific testing. <br>
Mitigation: Test Telegram alert delivery before relying on it for operational review. <br>
Risk: The plugin depends on the external hopeid package and host OpenClaw behavior. <br>
Mitigation: Use a pinned and reviewed hopeid dependency on a patched OpenClaw host. <br>


## Reference(s): <br>
- [ClawHub package page](https://clawhub.ai/emberdesire/skills/hopeids) <br>
- [hopeIDS GitHub repository](https://github.com/E-x-O-Entertainment-Studios-Inc/hopeIDS) <br>
- [hopeid npm package](https://www.npmjs.com/package/hopeid) <br>
- [hopeIDS documentation](https://exohaven.online/products/hopeids) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown command responses, JSON tool and gateway responses, shell command snippets, and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk scores, recommended actions, intent labels, notifications, quarantine identifiers, and metadata-only quarantine records.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
