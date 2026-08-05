## Description: <br>
Cross-platform screen sharing, remote desktop control, and real-time monitoring for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[swordlonn](https://clawhub.ai/user/swordlonn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to start screen sharing, create remote viewing links, and optionally allow trusted remote mouse and keyboard control across Windows, macOS, and Linux. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose the user's screen and, in control mode, allow mouse and keyboard actions. <br>
Mitigation: Use view-only mode unless the controller is fully trusted, and avoid running sessions while credentials or private documents are visible. <br>
Risk: Generated session links and local bridge access are sensitive because they may permit viewing or controlling the desktop. <br>
Mitigation: Treat session links as secrets, share them only with intended viewers, and end sessions when monitoring is complete. <br>
Risk: The security scan reports weak scoping and authentication around powerful local capture and control paths. <br>
Mitigation: Review before installation; publishers should bind the bridge explicitly to 127.0.0.1, authenticate sensitive routes, avoid public token exposure, and make control, audio, and auto-start behaviors explicit opt-ins. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/swordlonn/skills/skill) <br>
- [Publisher profile](https://clawhub.ai/user/swordlonn) <br>
- [Server-resolved GitHub provenance](https://github.com/SwordLonn/WatchItAI/tree/main/skill) <br>
- [WatchItAI website](https://watchitai.net) <br>
- [WatchItAI host page](https://watchitai.net/host) <br>
- [GitHub releases](https://github.com/SwordLonn/WatchItAI/releases) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated session links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May output a marked WatchItAI session URL that the agent should present as a Markdown link rather than plain text.] <br>

## Skill Version(s): <br>
0.1.0 (source: target metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
