## Description: <br>
Pushes all branches in a stack and opens or updates one dependent GitHub pull request per slice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill after creating a stacked branch topology to publish each slice, create draft dependent pull requests, and post a stack summary for reviewers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can push branches or create pull requests against the wrong repository, remote, stack prefix, base branch, or GitHub account. <br>
Mitigation: Confirm the repository, origin remote, STACK value, BASE branch, and authenticated gh account before running push or pull request commands. <br>
Risk: The optional jj git push --all accelerator may push more refs than the stack-specific loop. <br>
Mitigation: Prefer the stack-specific git push loop for routine use, or inspect refs carefully before using jj git push --all. <br>
Risk: Generated pull request titles, bodies, and stack summary comments may be incomplete or misleading. <br>
Mitigation: Keep pull requests as drafts until titles, descriptions, branch ordering, and summary comments have been reviewed. <br>


## Reference(s): <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-push) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline bash command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Git, GitHub CLI, and optional jj command examples; the agent should review the repository, remote, stack prefix, base branch, and account before use.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
