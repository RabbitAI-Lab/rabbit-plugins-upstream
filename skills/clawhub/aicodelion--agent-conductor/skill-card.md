## Description: <br>
Agent Conductor provides templates and guidance for orchestrating CLI-based coding sub-agents on implementation, scripting, data processing, and multi-stage workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[AICodeLion](https://clawhub.ai/user/AICodeLion) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to plan, delegate, coordinate, and validate coding-agent work across file edits, scripts, data pipelines, and staged implementation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegated agents may modify files or run commands beyond the user's intended scope. <br>
Mitigation: Require explicit approval for file writes and command execution, restrict work to trusted directories, and review all generated changes before accepting them. <br>
Risk: Long-running or parallel background jobs may consume resources or continue after the orchestrator loses context. <br>
Mitigation: Cap background jobs, keep concurrency low, record progress, and verify completion through logs and expected output files. <br>
Risk: Task prompts or delegated workflows may expose secrets or production credentials to sub-agents. <br>
Mitigation: Avoid passing secrets or production credentials in delegated task context and use least-privilege local environment configuration. <br>


## Reference(s): <br>
- [Patterns Reference](references/patterns.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/AICodeLion/agent-conductor) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with dispatch templates, checklists, tables, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent task specifications and validation guidance; does not itself execute delegated work.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
