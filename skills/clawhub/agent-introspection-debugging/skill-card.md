## Description: <br>
Debug agent behavior through a four-stage self-diagnosis loop: capture, diagnose, recover, and report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to structure self-debugging when an agent encounters repeated tool failures, context pressure, environment mismatches, or uncertain recovery paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may encourage an agent to inspect local workspace and service state while debugging. <br>
Mitigation: Keep inspection limited to task-relevant files, commands, and services, and avoid collecting credentials or unrelated local data. <br>
Risk: Debugging reports may record failure details, environment assumptions, or lessons learned. <br>
Mitigation: Review and redact sensitive paths, tokens, private data, and unrelated operational details before sharing or storing reports. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown diagnostic notes and recovery reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces failure capture, root-cause hypothesis, contained recovery action, and evidence of the resulting state.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
