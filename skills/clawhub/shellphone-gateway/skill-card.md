## Description: <br>
Shellphone Gateway guides agents through setting up a private WebSocket gateway between iOS devices and self-hosted AI bots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loserbcc](https://clawhub.ai/user/loserbcc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and self-hosting users use this skill to run the gateway, connect the ShellPhone iOS TestFlight app, and route mobile requests to local AI agents such as Ollama-backed bots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Speech features use ScrappyLabs, so audio or text may leave the self-hosted environment despite privacy-first messaging. <br>
Mitigation: Before deployment, confirm whether ScrappyLabs is optional, what data it receives, and how to disable TTS/ASR when third-party processing is not acceptable. <br>
Risk: Installation depends on external GitHub, PyPI, Docker Compose, and TestFlight artifacts that are not verified by the release evidence. <br>
Mitigation: Verify the repository, package, Compose file, and TestFlight publisher before installing or sharing connection tokens. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/loserbcc/skills/shellphone-gateway) <br>
- [ShellPhone TestFlight](https://testflight.apple.com/join/BnjD4BEf) <br>
- [Gateway GitHub](https://github.com/loserbcc/openclaw-gateway) <br>
- [ScrappyLabs](https://scrappylabs.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash commands, URLs, and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Docker and Python setup paths plus iOS TestFlight and QR-code connection steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
