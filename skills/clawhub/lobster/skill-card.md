## Description: <br>
Lobster workflow runtime for deterministic pipelines with approval gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guwidoe](https://clawhub.ai/user/guwidoe) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Lobster to run deterministic multi-step workflows, monitor pull requests or issues, process typed JSON pipelines, triage batches such as email, and pause for human approval before side effects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lobster pipelines can run shell commands and workflow steps with side effects. <br>
Mitigation: Review shell commands and workflow files before running them, and add approval gates before side-effecting steps. <br>
Risk: Clawdbot invocation can use credentials to call external tools or perform actions. <br>
Mitigation: Review clawd.invoke calls before execution and use scoped CLAWD tokens. <br>
Risk: Workflow state may persist sensitive data under the Lobster state directory. <br>
Mitigation: Relocate or clear ~/.lobster/state/ when stored workflow state may be sensitive. <br>


## Reference(s): <br>
- [ClawHub Lobster Skill Page](https://clawhub.ai/guwidoe/skills/lobster) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and YAML workflow examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe Lobster pipelines, workflow files, approval resumes, CLI usage, state configuration, and Clawdbot integration settings.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
