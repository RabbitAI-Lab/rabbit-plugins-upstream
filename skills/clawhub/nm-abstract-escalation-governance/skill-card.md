## Description: <br>
Assess whether to escalate models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide when model escalation is justified, document the reason for escalation, and return to a more efficient model after the deeper reasoning task is complete. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the advisory model-selection guidance as a substitute for evaluating the specific task context. <br>
Mitigation: Require documented investigation, escalation scope, and success criteria before changing model capability. <br>
Risk: The skill references an optional external plugin that is outside the scanned artifact. <br>
Mitigation: Evaluate and scan the external plugin separately before installing or relying on it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-escalation-governance) <br>
- [clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with YAML configuration examples and decision tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory model-selection guidance; no code execution, credential handling, or hidden data access is described in the security evidence.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
