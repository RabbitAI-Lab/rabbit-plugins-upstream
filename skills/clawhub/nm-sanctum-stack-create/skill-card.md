## Description: <br>
Initializes a stacked branch set from an ordered plan, one branch per slice with parent-child links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to convert an ordered implementation plan into a local stacked Git branch structure, with one dependent branch per slice and verification steps before work continues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to create and switch Git branches in the current repository, which can disrupt local work if run from the wrong branch or a dirty working tree. <br>
Mitigation: Use it only on a clean working tree, verify the base branch and generated branch names before branch creation, and review the resulting stack topology. <br>
Risk: Pushing empty slice branches can create confusing pull requests. <br>
Mitigation: Create at least one commit on each slice branch before pushing the stack. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-create) <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides branch planning, local branch creation, and stack verification; it does not execute commands itself.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
