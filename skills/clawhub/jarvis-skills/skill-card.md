## Description: <br>
JARVIS AI Skills helps agents guide OpenClaw-based robotic arm and gripper control through voice or code, including movement, gripping, sensing, collision detection, sequencing, and simulation-oriented workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aly-joseph](https://clawhub.ai/user/aly-joseph) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, robotics engineers, and operators use this skill to plan and integrate OpenClaw robotic arm and gripper actions through code snippets or voice-command patterns. It is suited to controlled robotics workflows where motion limits, simulation, operator confirmation, and hardware safety checks are handled before any physical execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Physical robotic arm or gripper motion can injure people or damage equipment if run without workspace limits, speed and force caps, or explicit operator confirmation. <br>
Mitigation: Treat the skill as simulation-only until the control path is independently audited and emergency stop, access control, workspace bounds, speed limits, force limits, and per-motion confirmation are in place. <br>
Risk: The artifact references a required control module that is not included, so real hardware behavior cannot be verified from the submitted files alone. <br>
Mitigation: Review the missing control module and hardware integration before installation, and validate all commands in simulation before connecting to physical devices. <br>
Risk: Voice-driven commands can trigger unintended movement if commands are misrecognized or issued in an unsafe environment. <br>
Mitigation: Require explicit operator confirmation for each movement or gripper action and restrict voice control to supervised, access-controlled settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aly-joseph/skills/jarvis-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with Python code snippets and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include robotic motion examples, voice-command phrasing, dependency notes, and safety review guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact files list 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
