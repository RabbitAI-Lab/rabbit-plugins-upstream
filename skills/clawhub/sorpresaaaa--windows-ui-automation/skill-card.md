## Description: <br>
Automates Windows desktop mouse, keyboard, and window interactions using PowerShell. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sorpresaaaa](https://clawhub.ai/user/sorpresaaaa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users can use this skill to simulate desktop input, type into non-web applications, click controls, and manage basic window focus workflows on Windows systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send mouse and keyboard input to the live Windows desktop, including sensitive or elevated prompts. <br>
Mitigation: Install it only when supervised desktop control is intended, avoid using it around sensitive prompts, and review planned typing or clicking before execution. <br>
Risk: Automation can change files, settings, accounts, or external services if the wrong window is focused. <br>
Mitigation: Confirm the intended window is focused and verify desktop state before and after complex UI actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sorpresaaaa/skills/windows-ui-automation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with PowerShell command examples and script snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance and PowerShell invocations for Windows UI automation; resulting actions can affect the live desktop state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
