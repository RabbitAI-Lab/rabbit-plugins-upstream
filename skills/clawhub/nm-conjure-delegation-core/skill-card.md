## Description: <br>
Delegates tasks to Gemini or Qwen with quota tracking and error handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide when external LLM delegation is appropriate, plan handoffs, estimate costs, and validate delegated results before integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegation may expose secrets or sensitive data to external LLM services. <br>
Mitigation: Review each delegation plan before execution, redact sensitive inputs, and avoid sending secrets or sensitive data. <br>
Risk: Delegated outputs may be incorrect, incomplete, or misleading. <br>
Mitigation: Validate output format and correctness before integration, and keep high-reasoning or security-sensitive work local. <br>
Risk: OAuth client secrets and service credentials may be mishandled during setup. <br>
Mitigation: Handle OAuth and client secrets carefully, verify authentication prerequisites, and prefer redacted audit logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-delegation-core) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with checklists, decision matrices, templates, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces delegation plans, suitability assessments, cost estimates, troubleshooting steps, and validation guidance.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
