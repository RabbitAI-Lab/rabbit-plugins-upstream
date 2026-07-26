## Description: <br>
Interact with the desktop GUI by taking screenshots, listing or raising windows, clicking with grid targeting, typing text, and pressing key combinations; all commands return JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zachrouan](https://clawhub.ai/user/zachrouan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect and control a live desktop GUI through screenshots, window focus, grid-based clicks, text entry, and key presses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect and control a live desktop, including screenshots, window focus, clicks, typing, and keyboard shortcuts. <br>
Mitigation: Use only in supervised sessions and avoid private windows, passwords, financial or administrative workflows, and irreversible form submissions unless explicitly approved. <br>
Risk: Grid-targeted clicks can miss if the selected crosshair is not on the intended control. <br>
Mitigation: Use the orient, zoom, click, and verify loop; re-check state after each action before continuing. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zachrouan/skills/gui-tool) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown instructions with bash command examples; CLI command outputs are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Screenshots are written to caller-selected file paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
