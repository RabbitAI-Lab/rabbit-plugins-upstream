## Description: <br>
Provides full desktop GUI control for headless Linux servers using Xvfb, XFCE, xdotool actions, and optional VNC viewing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ram-raghav-s](https://clawhub.ai/user/ram-raghav-s) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to create and control a virtual Linux desktop on headless servers, including screenshots, mouse actions, typing, scrolling, keyboard input, and live VNC viewing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent remote desktop services with weak access controls can expose the controlled desktop if deployed on an accessible network interface. <br>
Mitigation: Install only on a dedicated disposable server or VM, add VNC/noVNC authentication, and bind access to localhost or a firewall-restricted interface before use. <br>
Risk: The setup process makes broad system-level changes, including persistent systemd services and changes related to the XFCE desktop. <br>
Mitigation: Inspect setup-vnc.sh before running it and prepare rollback steps to disable the services and restore /usr/bin/xfdesktop. <br>


## Reference(s): <br>
- [Computer Use Skill Page](https://clawhub.ai/ram-raghav-s/skills/computer-use) <br>
- [Google Chrome Linux Package](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, Images] <br>
**Output Format:** [Shell scripts and command output, including base64-encoded PNG screenshots] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses DISPLAY=:99 with a 1024x768 virtual desktop; most actions return a screenshot after a short delay.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
