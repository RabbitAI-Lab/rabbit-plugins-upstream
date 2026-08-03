## Description: <br>
Initializes a stacked branch set from an ordered plan, one branch per slice with parent-child links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn an ordered implementation plan into a stacked Git branch set, with each branch representing one dependent slice of work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to create and switch local Git branches, changing repository state. <br>
Mitigation: Use it only for intended stacked-branch workflows, start from a clean working tree, and review the proposed branch names and topology before commands run. <br>
Risk: Broad triggers such as git, pr, branches, and planning may activate the skill during ordinary repository discussions. <br>
Mitigation: Narrow activation triggers or invoke the skill explicitly when accidental activation would disrupt normal Git or pull request work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-create) <br>
- [claude-night-market sanctum plugin](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides Git and optional jj commands, branch naming conventions, and progress-tracking labels for a stacked-branch workflow.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
