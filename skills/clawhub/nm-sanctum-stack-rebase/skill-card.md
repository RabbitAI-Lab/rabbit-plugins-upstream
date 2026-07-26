## Description: <br>
Cascades a rebase through an entire PR stack after a base PR merges or upstream changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers maintaining stacked pull requests use this skill to rebase local slice branches after base branch, root PR, or mid-stack changes and to update PR bases when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Force-pushing rebased stack branches can rewrite shared branch history or affect branches outside the intended stack. <br>
Mitigation: Fetch first, confirm the branch pattern matches only the intended stack, verify collaborators are not depending on old branch history, and use force-with-lease safeguards. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-rebase) <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes git rebase, force-push, and PR base update guidance that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
