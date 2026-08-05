## Description: <br>
Advanced browser automation via the Camoufox Firefox fork for authorized automation tasks that encounter bot protection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akdira](https://clawhub.ai/user/akdira) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to drive OpenClaw browser automation through Camoufox when authorized workflows need tabs, snapshots, clicks, typing, navigation, screenshots, JavaScript evaluation, or cookie-backed sessions on bot-hardened websites. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Anti-detection browser automation can be misused or violate site authorization and terms. <br>
Mitigation: Use only for approved automation on services where authorization and applicable terms have been confirmed. <br>
Risk: Imported cookie files can provide full account access if exposed. <br>
Mitigation: Protect cookie files with owner-only permissions, keep them outside shared temporary locations, and delete them when the task is complete. <br>
Risk: The local automation server may expose sensitive browser controls if reachable by untrusted clients. <br>
Mitigation: Bind the service to localhost, avoid exposing port 9377, and require an API key or gateway control for sensitive operations. <br>
Risk: Crash telemetry or browsing artifacts may be inappropriate in sensitive environments. <br>
Mitigation: Disable telemetry where required and avoid retaining screenshots, logs, cookies, or temporary browsing artifacts longer than necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/akdira/skills/camofox-default-browser) <br>
- [Camoufox browser repository](https://github.com/jo-inc/camofox-browser) <br>
- [Camoufox releases](https://github.com/jo-inc/camofox/releases) <br>
- [AGENTS.md](artifact/AGENTS.md) <br>
- [API.md](artifact/API.md) <br>
- [CONFIGURATION.md](artifact/CONFIGURATION.md) <br>
- [INSTALL.md](artifact/INSTALL.md) <br>
- [SECURITY.md](artifact/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, API calls, Code, Markdown, Guidance] <br>
**Output Format:** [Markdown with JSON examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing tool guidance for Camoufox browser automation, including tab control, snapshots, navigation, screenshots, JavaScript evaluation, cookie import, installation, and security practices.] <br>

## Skill Version(s): <br>
1.1.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
