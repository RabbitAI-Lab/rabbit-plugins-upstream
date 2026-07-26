## Description: <br>
Git Helper gives agents concise guidance for common Git operations such as status, pull, push, branch management, and log viewing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to ask an agent for concise Git command guidance for repository status, synchronization, push, branch, and log workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Git operations such as pull, push, and branch changes can alter repository state or publish local commits. <br>
Mitigation: Before acting on guidance from this skill, confirm the repository, branch, remote, and intended effect. <br>
Risk: The artifact documents a git-helper command but does not include that executable. <br>
Mitigation: Verify what git-helper resolves to in the local environment before running any documented command. <br>


## Reference(s): <br>
- [Git Helper on ClawHub](https://clawhub.ai/xejrax/skills/git-helper) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the git binary; no executable helper is included in the artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
