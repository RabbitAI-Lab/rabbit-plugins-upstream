## Description: <br>
PPT Generator creates editable PowerPoint presentations from JSON, with 11 slide types, five color schemes, and support for charts, tables, timelines, and images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content authors, and agents use this skill to turn structured JSON slide descriptions into editable PPTX decks for reports, presentations, academic talks, and technical sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local workflow that reads JSON and local image paths and writes a PPTX file. <br>
Mitigation: Run it in an environment appropriate to the task, review the requested file paths, and inspect the generated deck before sharing it. <br>
Risk: Malformed or inaccurate input JSON can produce an incomplete or misleading presentation. <br>
Mitigation: Validate the input JSON and review generated slides for content, layout, and data accuracy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tobewin/skills/pptx-generator) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [Editable PPTX file generated from JSON input, with optional command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and python-pptx; image slides read local image paths supplied in the JSON input.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
