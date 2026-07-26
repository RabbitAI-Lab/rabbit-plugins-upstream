## Description: <br>
Helps quality, process, and customer-quality engineers create targeted rework or repair disposition plans for specific nonconforming products using objective defect information and customer requirements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers, process engineers, customer-quality engineers, MRB members, and manufacturing supervisors use this skill to draft controlled disposition plans after a specific batch or item has been found nonconforming. It helps structure the decision, repair or rework steps, verification criteria, traceability, and escalation points around the customer requirements provided by the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated disposition could be treated as an approval decision rather than a drafting aid. <br>
Mitigation: Require authorized quality, MRB, or customer-facing personnel to confirm requirements, acceptance criteria, and approval obligations before operational use. <br>
Risk: Report file generation may not run as described because the referenced report-building script is not included in the package. <br>
Mitigation: Have the agent produce the plain text and Markdown report contents directly when the script is unavailable. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-rework-repair-plan) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-rework-repair-plan) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Plain text and Markdown disposition reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires objective nonconformity information and customer requirements before generating a plan; missing details are marked for user completion.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
