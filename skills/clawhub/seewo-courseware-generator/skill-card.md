## Description: <br>
Generates native, editable Seewo Whiteboard (.enbx) courseware from a lesson topic, outline, or free-form teaching description. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[insistandtry](https://clawhub.ai/user/insistandtry) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, instructional designers, and agents assisting them use this skill to turn lesson content into native Seewo Whiteboard courseware and validate the generated package before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local image paths included in the JSON courseware spec are embedded into the generated .enbx file. <br>
Mitigation: Only include local files that are intended to be shared with the courseware. <br>
Risk: Hardcoded example paths in the skill instructions may not match another user's environment. <br>
Mitigation: Adjust paths before running the generator and validate the resulting .enbx file before delivery. <br>


## Reference(s): <br>
- [ENBX courseware format reference](artifact/references/enbx_format.md) <br>
- [ClawHub skill page](https://clawhub.ai/insistandtry/skills/seewo-courseware-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with JSON specifications, shell commands, and generated .enbx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a native Seewo Whiteboard .enbx package and validation output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
