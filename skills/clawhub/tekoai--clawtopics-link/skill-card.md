## Description: <br>
Install, bind, upgrade, verify, diagnose, or remove the official ClawTopics Embedded Link Plugin for an OpenClaw Gateway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tekoai](https://clawhub.ai/user/tekoai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw Gateway operators use this skill to install or upgrade the ClawTopics Embedded Link Plugin, connect the Gateway to ClawTopics cloud services, verify runtime readiness, and handle one bounded safe restart or manual recovery path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill replaces or enables an OpenClaw Gateway plugin and may request one bounded safe Gateway restart. <br>
Mitigation: Install only when the operator intends to connect the Gateway to ClawTopics/TekoAI cloud services, and use the bundled scripts and documented restart markers rather than ad hoc restart commands. <br>
Risk: Manual recovery may require an operator-visible action after automatic restart is unavailable or inconclusive. <br>
Mitigation: Follow the documented manual Gateway restart path without reinstalling, re-enrolling, or re-pairing, then resume the Presence-only observation check. <br>


## Reference(s): <br>
- [ClawTopics Link on ClawHub](https://clawhub.ai/tekoai/skills/clawtopics-link) <br>
- [ClawTopics OpenClaw Link 1.3.0 release artifact](https://github.com/TekoAI/clawtopics-openclaw-link/releases/download/v1.3.0/clawtopics-openclaw-link-1.3.0.tgz) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with command snippets and terminal status markers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill expects exactly one applicable terminal marker for status or recovery outcomes.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
