## Description: <br>
Delegates tasks to Qwen CLI via delegation-core for Alibaba's models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to delegate large-context analysis, summarization, batch processing, and multi-file review tasks to a configured Qwen CLI environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected prompts and file contents can be processed by the external Qwen CLI or provider. <br>
Mitigation: Limit delegated prompts and file sets to intended, non-sensitive material and review what will be sent before execution. <br>
Risk: Broad activation triggers such as cli can make the skill available in situations where Qwen delegation was not intended. <br>
Mitigation: Narrow or disable generic triggers and invoke Qwen delegation explicitly when that behavior is desired. <br>
Risk: Delegated model output can be incomplete, incorrect, or unsuitable for direct application. <br>
Mitigation: Review Qwen responses before applying generated code, configuration, or operational guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-qwen-delegation) <br>
- [Conjure homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash command examples and CLI usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output may include Qwen CLI commands, model selection guidance, authentication setup, and delegation patterns; structured output depends on the requested Qwen format.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
