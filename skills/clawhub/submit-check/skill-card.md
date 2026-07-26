## Description: <br>
Find students who haven't submitted artifacts by matching filenames against a class manifest. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericli98](https://clawhub.ai/user/ericli98) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, teaching assistants, or operations staff use this skill to identify missing student submissions by comparing artifact filenames or exported filename lists against a class CSV manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Class manifests and artifact filenames may contain student identifiers or names. <br>
Mitigation: Use the skill only with authorized class data and avoid sharing generated missing-student reports beyond authorized course staff. <br>
Risk: Filename matching can produce false positives or false negatives when names or codes overlap or submissions use unexpected filenames. <br>
Mitigation: Review the submitted and missing lists before taking administrative action, and adjust matching mode or manifest data when needed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain-text submission summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operates on local class manifests and artifact filenames supplied by the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
