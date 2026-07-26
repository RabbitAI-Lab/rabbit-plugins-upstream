## Description: <br>
Safe Execution is advertised as a safety and cost-control skill for detecting repeated tool-call loops, estimating task cost, and protecting exception paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laolong507](https://clawhub.ai/user/laolong507) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users and developers use this skill as safety guidance intended to stop repeated failing tool-call loops before they drain user balance. The packaged release should be reviewed before relying on it because the server security summary says the main SKILL.md file is empty and the skill is likely nonfunctional. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is likely nonfunctional because the main SKILL.md file is empty. <br>
Mitigation: Inspect the installed package before use and require the publisher to provide real SKILL.md instructions before relying on loop or cost protection. <br>
Risk: Users may assume the advertised loop and cost protections are active when the package may not enforce them. <br>
Mitigation: Validate the skill with a controlled failing-tool-call scenario and stop deployment if it does not halt after the expected repeated failures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/laolong507/skills/safe-execution) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The submitted package has an empty SKILL.md, so expected runtime guidance may be absent until the publisher supplies real skill instructions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
