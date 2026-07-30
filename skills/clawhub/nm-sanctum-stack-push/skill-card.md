## Description: <br>
Pushes all branches in a stack and opens or updates one dependent PR per slice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill after creating a stacked branch topology to push each slice branch, open or update dependent draft pull requests, and post a stack summary on GitHub. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can push branches, create draft pull requests, and add a GitHub PR comment using the active repository and authenticated account. <br>
Mitigation: Confirm the repository, remote, stack prefix, base branch, and GitHub authentication account before running the commands. <br>
Risk: Republishing after rebases can overwrite remote branch history if the wrong push mode is used. <br>
Mitigation: Use git push --force-with-lease for rebased stack branches and avoid plain --force. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-push) <br>
- [Night Market sanctum homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an existing Git branch stack, a GitHub remote, and an authenticated gh CLI session.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
