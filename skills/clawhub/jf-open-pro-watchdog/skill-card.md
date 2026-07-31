## Description: <br>
JF Watchdog monitors user-defined camera regions with JF device snapshots and AI visual analysis for anti-theft, passage occupancy, and presence checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to configure JF camera regions, capture baseline and current images, and receive patrol reports that flag missing, appeared, changed, or indeterminate conditions. <br>

### Deployment Geography for Use: <br>
China Mainland (CN), Asia (AS), Europe (EU), and North America (NA) <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled patrol instructions may expose API secrets if copied with plaintext credentials. <br>
Mitigation: Inject credentials at runtime from a secret manager or protected environment variables, and avoid storing populated task templates. <br>
Risk: The skill handles real camera snapshots, baseline images, device identifiers, and patrol reports. <br>
Mitigation: Define retention, access, and sharing rules for captured images and reports before deployment. <br>
Risk: Device passwords and API credentials are required for capture workflows. <br>
Mitigation: Keep credentials out of command history and configuration files, rotate them regularly, and restrict them to the minimum device scope needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-watchdog) <br>
- [JF Open Platform documentation](https://docs.jftech.com) <br>
- [JF cloud snapshot pricing](https://aops.jftech.com/#/pricing?lang=zh&tab=MEDIA_PROCESSING) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with JSON command output, shell commands, configuration snippets, and generated image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local capture images, cropped baseline images, cropped current-region images, and annotated patrol images.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact metadata reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
