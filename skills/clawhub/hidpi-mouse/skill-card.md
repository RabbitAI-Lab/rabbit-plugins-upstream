## Description: <br>
Universal HiDPI mouse click handling for Linux desktop automation that auto-detects or calibrates scale factors and converts Claude display coordinates to xdotool screen coordinates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeyuyuyu](https://clawhub.ai/user/zeyuyuyu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use HiDPI Mouse to convert displayed screenshot coordinates into accurate Linux/X11 mouse movement, clicks, and drags across standard and HiDPI displays. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move, click, and drag on a live Linux/X11 desktop, which can activate unintended controls if coordinates are wrong or sensitive screens are open. <br>
Mitigation: Supervise use, calibrate before important actions, verify coordinates on sensitive screens, and avoid running the scripts with elevated privileges. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zeyuyuyu/skills/hidpi-mouse) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Shell script execution with plain-text status messages and optional configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Linux/X11 desktop access with xdotool, scrot, and python3.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
