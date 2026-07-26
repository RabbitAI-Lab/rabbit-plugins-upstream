## Description: <br>
Native Windows mouse control for moving, clicking, and dragging the pointer through local Win32 scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lurklight](https://clawhub.ai/user/lurklight) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators using a Windows desktop can ask an agent to move the pointer, click, or drag when automating local UI workflows. It is best suited to explicit coordinates or small supervised pointer actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill allows an agent to move and click the Windows mouse, which can affect sensitive screens such as payment pages, permission prompts, and account settings. <br>
Mitigation: Install only when mouse control is intended, use explicit coordinates or verified targets, and supervise clicks or drags on sensitive screens. <br>
Risk: The bundle ships scripts as text that must be saved as executable files before use. <br>
Mitigation: Review the .cmd and .ps1 text before saving them as executable scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lurklight/skills/win-mouse-native) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with command examples and one-line JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Windows only; requires saving the provided text files as executable .cmd and .ps1 scripts before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
