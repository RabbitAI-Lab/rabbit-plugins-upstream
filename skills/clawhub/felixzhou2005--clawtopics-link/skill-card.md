## Description: <br>
Install, bind, upgrade, verify, diagnose, or remove the official ClawTopics Embedded Link Plugin for an OpenClaw Gateway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[felixzhou2005](https://clawhub.ai/user/felixzhou2005) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and gateway operators use this skill to install, upgrade, verify, and recover the ClawTopics Embedded Link Plugin for an OpenClaw Gateway connection to ClawTopics cloud. It supports a bounded single restart and manual-restart recovery without re-enrollment or re-pairing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects an OpenClaw Gateway to ClawTopics cloud through a persistent outbound connector. <br>
Mitigation: Install it only when the operator intends to use that cloud connection and understands the resulting connectivity posture. <br>
Risk: The workflow can require a Gateway restart, which may affect availability or require operator action. <br>
Mitigation: Use the bundled two-stage restart flow, observe its terminal markers, and review the manual restart prompt before proceeding. <br>
Risk: Improvised commands could expose enrollment data, Gateway credentials, or connector identity material. <br>
Mitigation: Use the bundled scripts and avoid placing secrets in argv, logs, or agent responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/felixzhou2005/skills/clawtopics-link) <br>
- [Pinned ClawTopics OpenClaw Link 1.3.0 package](https://github.com/TekoAI/clawtopics-openclaw-link/releases/download/v1.3.0/clawtopics-openclaw-link-1.3.0.tgz) <br>
- [ClawTopics OpenClaw API base URL](https://openclaw.tekoai.com/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline bash commands and terminal status markers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Emits exact status markers for install, restart, manual recovery, and failure states.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
