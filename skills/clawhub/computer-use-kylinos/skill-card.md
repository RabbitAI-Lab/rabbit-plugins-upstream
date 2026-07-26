## Description: <br>
GUI automation on KylinOS. V11 (Wayland/wlcom) uses wlcctrl; V10SP1 (X11) uses xdotool. Find/launch/focus windows, screenshot, click/type/drag with correct coordinates, and verify GUI results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyanogenic](https://clawhub.ai/user/cyanogenic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect and control KylinOS desktop sessions across V11 Wayland and V10SP1 X11. It supports finding windows, capturing screenshots, calculating relative coordinates, clicking, typing, dragging, and verifying GUI outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Desktop automation can expose window names and window captures or interact with sensitive applications. <br>
Mitigation: Use the skill only in sessions where desktop control is acceptable, keep unrelated sensitive applications closed, and verify the target window before capturing or acting. <br>
Risk: Pointer and keyboard automation can click, type, drag, move windows, or submit changes in the wrong UI context. <br>
Mitigation: Confirm window identifiers and screenshot-derived coordinates before execution, prefer predictable keyboard input when available, and avoid closing or killing windows unless explicitly requested. <br>


## Reference(s): <br>
- [KylinOS GUI Automation Details](references/details.md) <br>
- [Computer Use Kylinos ClawHub Page](https://clawhub.ai/cyanogenic/skills/computer-use-kylinos) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces command-oriented desktop automation guidance for KylinOS V11 Wayland and V10SP1 X11.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
