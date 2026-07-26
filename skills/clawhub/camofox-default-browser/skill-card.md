## Description: <br>
Anti-detection browser automation via Camoufox Firefox fork — bypasses Cloudflare, captcha, and bot blocking <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akdira](https://clawhub.ai/user/akdira) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to route OpenClaw browser automation through Camoufox for authorized work on sites where standard browser automation is blocked or challenged. It provides tab control, navigation, snapshots, screenshots, JavaScript evaluation, and optional cookie import through the camofox tool set. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Anti-detection browser automation can be used to bypass site protections or terms where the user lacks authorization. <br>
Mitigation: Install and use only for authorized automation, and do not use it to bypass protections on sites where permission is absent. <br>
Risk: Imported cookie files can grant live access to user accounts. <br>
Mitigation: Keep cookie import disabled unless needed, protect cookie files as credentials, and require CAMOFOX_API_KEY when enabling the import endpoint. <br>
Risk: The local background server exposes browser-control routes if access controls are not configured. <br>
Mitigation: Use CAMOFOX_ACCESS_KEY or equivalent local access controls and restrict server exposure to trusted local callers. <br>
Risk: Telemetry or persisted browser profiles may create privacy or compliance concerns. <br>
Mitigation: Review crash telemetry and profile persistence settings, and disable telemetry with CAMOFOX_CRASH_REPORT_ENABLED=false when required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/akdira/skills/camofox-default-browser) <br>
- [Artifact-declared Camoufox browser homepage](https://github.com/jo-inc/camofox-browser) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-like tool parameters and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for using camofox browser automation tools; screenshots may be returned as base64 by the underlying tool.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
