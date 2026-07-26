## Description: <br>
Local browser and Windows desktop control for Mavis. Uses the official Microsoft playwright-cli (a11y-tree based, no screenshot flash) for browser automation, and a PowerShell + .NET helper for Windows desktop (mouse, keyboard, screenshots, windows, clipboard, run). Includes a unified `mcp.cjs` dispatcher with shortcuts for the common operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fvegiard](https://clawhub.ai/user/fvegiard) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical operators use this skill to give an agent local control over a browser session and Windows desktop tasks, including page navigation, accessibility-tree interaction, screenshots, window focus, clipboard operations, and shell execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent shell-level control of a Windows machine, including command and PowerShell execution. <br>
Mitigation: Install only when that level of local control is acceptable, use a low-risk environment, and closely review workflows before execution. <br>
Risk: Browser automation over CDP can see and act on the connected Edge session, including logged-in sites. <br>
Mitigation: Avoid sensitive accounts or private data unless necessary, and inspect browser targets before allowing actions. <br>
Risk: Desktop screenshots, clicks, keyboard input, clipboard changes, and window activation affect the user's actual desktop. <br>
Mitigation: Run under user supervision and keep unrelated or sensitive desktop content out of scope. <br>


## Reference(s): <br>
- [Source repository](https://github.com/fvegiard/mavis-tools) <br>
- [ClawHub skill page](https://clawhub.ai/fvegiard/skills/mavis-tools) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct browser automation, desktop interaction, clipboard access, screenshots, and local command execution through the described helpers.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
