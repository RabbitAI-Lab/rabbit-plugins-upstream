## Description: <br>
Resume Builder helps an agent gather resume details through a guided conversation and produce Reactive Resume-compatible JSON for import into Reactive Resume. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amruthpillai](https://clawhub.ai/user/amruthpillai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, job seekers, and agents use this skill to create structured resumes by collecting user-provided profile, experience, education, skills, and layout preferences. It is intended to produce import-ready Reactive Resume JSON while asking clarifying questions instead of inventing missing details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume creation can involve sensitive personal details such as contact information, locations, private links, or references. <br>
Mitigation: Share only details intended for the final resume, and use placeholders or omit sensitive fields until ready to export or import the resume. <br>
Risk: Incomplete or ambiguous user input can lead to missing fields or invalid Reactive Resume JSON. <br>
Mitigation: Ask clarifying questions for missing details and validate the final JSON against the Reactive Resume schema before import. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/amruthpillai/skills/resume-builder) <br>
- [Reactive Resume](https://rxresu.me) <br>
- [Reactive Resume JSON Schema](https://rxresu.me/schema.json) <br>
- [Reactive Resume Schema Reference](artifact/references/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [Guided conversational prompts followed by a Reactive Resume JSON object.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The JSON should conform to the Reactive Resume schema and include only information provided or confirmed by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
