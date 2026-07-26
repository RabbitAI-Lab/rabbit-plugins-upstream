## Description: <br>
Prepares pull requests by running quality gates, drafting descriptions, and validating tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to prepare pull requests by reviewing workspace state, running quality gates, self-reviewing changes, documenting testing, and drafting a PR description. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may prepare GitHub-facing PR text or review evidence from local repository state. <br>
Mitigation: Review generated PR descriptions, comments, and any public GitHub writes before posting or publishing them. <br>
Risk: The workflow asks the agent to run project-specific formatting, linting, and test commands. <br>
Mitigation: Run commands only in a trusted workspace, inspect command intent first, and document skipped or failed checks with a mitigation plan. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-pr-prep) <br>
- [Night Market Sanctum plugin](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and checklist items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a PR description path and contents, with validation commands, testing notes, and checklist items.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
