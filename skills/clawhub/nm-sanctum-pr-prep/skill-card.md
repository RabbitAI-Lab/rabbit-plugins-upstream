## Description: <br>
Prepares pull requests by running quality gates, drafting descriptions, and validating tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare pull requests by reviewing workspace state, running project quality gates, summarizing changes, documenting tests, and drafting a PR description. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project-specific formatters, linters, and tests may modify workspace files or fail in ways that require follow-up changes. <br>
Mitigation: Review the planned commands before execution, inspect any resulting diffs, and re-run quality gates after fixes. <br>
Risk: The PR description output path may create or overwrite a file. <br>
Mitigation: Choose the output path deliberately and review the generated PR description before using it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-sanctum-pr-prep) <br>
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and checklist items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a PR description at a user-specified path and may report the file path and contents for confirmation.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
