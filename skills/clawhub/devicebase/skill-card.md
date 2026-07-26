## Description: <br>
Devicebase CLI is a cross-platform Go CLI for remote Android, HarmonyOS, and iOS device control via HTTP API, including tap, swipe, text input, app launching, screenshots, UI hierarchy inspection, and device information retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[richieone](https://clawhub.ai/user/richieone) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to install and operate Devicebase CLI for authorized remote mobile-device testing, mobile CI, and AI-agent workflows across Android, HarmonyOS, and iOS devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote installer scripts can execute code from Devicebase download URLs. <br>
Mitigation: Install only when Devicebase is trusted and review the installer before running it. <br>
Risk: DEVICEBASE_API_KEY can authorize remote device control if exposed. <br>
Mitigation: Keep DEVICEBASE_API_KEY private, avoid logging it, and rotate it if disclosure is suspected. <br>
Risk: Screenshots, UI hierarchy dumps, and text-entry commands can expose personal data, credentials, or private app state. <br>
Mitigation: Use the skill only on devices and accounts you are authorized to control, and redact or limit captured data. <br>


## Reference(s): <br>
- [Devicebase website](https://www.devicebase.cn/) <br>
- [Devicebase Linux and macOS installer](https://downloads.devicebase.cn/cli/install.sh) <br>
- [Devicebase Windows installer](https://downloads.devicebase.cn/cli/install.ps1) <br>
- [ClawHub skill page](https://clawhub.ai/richieone/skills/devicebase) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and command reference tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may produce screenshots, UI hierarchy JSON, and device information when executed against authorized devices.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
