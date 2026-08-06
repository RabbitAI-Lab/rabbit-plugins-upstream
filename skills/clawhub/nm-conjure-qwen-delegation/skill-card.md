## Description: <br>
Delegates tasks to Qwen CLI via delegation-core for Alibaba's models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to delegate large-context analysis, summarization, batch processing, and multi-file review tasks to Qwen CLI through the shared delegation-core workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Qwen delegation can send prompts and included file contents to the configured Qwen or Alibaba model service. <br>
Mitigation: Use narrow file selections, avoid broad globs over sensitive repositories, and review what will be included before delegation. <br>
Risk: QWEN_API_KEY or Qwen login credentials are required for some workflows. <br>
Mitigation: Manage Qwen credentials as sensitive secrets and avoid exposing them in prompts, shell history, logs, or committed files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-qwen-delegation) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>
- [Qwen-specific configuration](modules/qwen-specifics.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Qwen model choices, CLI options, authentication steps, and file inclusion patterns.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
