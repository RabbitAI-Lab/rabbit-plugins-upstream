## Description: <br>
Control Roborock robot vacuums through the roborock CLI for status checks, cleaning commands, maps, consumables, and settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dru-ca](https://clawhub.ai/user/dru-ca) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent prepare Roborock CLI commands for vacuum status, room cleaning, docking, map retrieval, maintenance checks, and settings changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on the python-roborock CLI having access to a Roborock or Xiaomi Home account and linked vacuums. <br>
Mitigation: Install it only if you trust the CLI, enter credentials only into the CLI prompt, and review account access before use. <br>
Risk: Cleaning and settings commands can affect the wrong vacuum or room if device or room IDs are mistaken. <br>
Mitigation: Confirm device and room IDs before running cleaning, docking, consumable reset, volume, DND, LED, or child-lock commands. <br>
Risk: Map images, room IDs, and device IDs can reveal private home layout or device information. <br>
Mitigation: Treat these values as private and avoid sharing saved map images or identifiers outside the intended environment. <br>


## Reference(s): <br>
- [python-roborock](https://github.com/humbertogontijo/python-roborock) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that control a physical vacuum and reference private device, room, or map identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
