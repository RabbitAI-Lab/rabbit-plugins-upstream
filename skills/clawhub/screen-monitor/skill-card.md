## Description: <br>
Dual-mode screen sharing and analysis for agents using multimodal vision models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emasoudy](https://clawhub.ai/user/emasoudy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to share a browser window, screen, or local screenshot for visual inspection and troubleshooting with a configured vision-capable model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive screen images with weak access controls and limited privacy disclosure. <br>
Mitigation: Use only on trusted networks and non-sensitive screens, prefer sharing a single window, and stop sharing when finished. <br>
Risk: Screenshots may be stored locally under /tmp and analyzed by the configured agent or model. <br>
Mitigation: Avoid sharing passwords, private messages, customer data, admin consoles, or regulated information, and clear temporary screenshots when the session is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/emasoudy/skills/screen-monitor) <br>
- [Screen sharing portal](web/screen-share.html) <br>
- [Frame storage server](references/backend-endpoint.js) <br>
- [Share URL helper](references/get-share-url.sh) <br>
- [Screen analysis helper](references/screen-analyze.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command invocations and local screenshot/image artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a vision-capable model, a modern browser with WebRTC, Node.js, curl, and optionally ImageMagick for OS screenshot fallback.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and manifest.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
