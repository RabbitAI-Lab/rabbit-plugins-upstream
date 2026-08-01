## Description: <br>
Delegates tasks to Gemini or Qwen with quota tracking and error handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide when to delegate low-complexity, large-context work to external LLM services and how to plan, validate, and integrate those results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegating prompts or files to external providers can expose secrets, private customer data, authentication code, or sensitive files. <br>
Mitigation: Review the data being delegated and use approved transfer and retention paths before sending sensitive material to external services. <br>
Risk: Delegated output can be incorrect, misleading, or unsuitable for tasks that require high-level reasoning. <br>
Mitigation: Keep architecture, strategy, design, nuanced review, and other high-complexity decisions local, and validate delegated results before integration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-delegation-core) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>
- [Task assessment module](modules/task-assessment.md) <br>
- [Handoff patterns module](modules/handoff-patterns.md) <br>
- [Cost estimation module](modules/cost-estimation.md) <br>
- [Troubleshooting module](modules/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with decision matrices, checklists, templates, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Delegation outputs are expected to be validated before integration.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release; artifact frontmatter is 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
