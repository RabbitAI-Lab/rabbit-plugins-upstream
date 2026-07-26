## Description: <br>
Interact with Gitea using the `tea` CLI. Use `tea issues`, `tea pulls`, `tea releases`, and other commands for issues, PRs, releases, and repository management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericxliu1990](https://clawhub.ai/user/ericxliu1990) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and repository maintainers use this skill to manage Gitea repositories, issues, pull requests, releases, actions, webhooks, and related project entities through `tea` CLI guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide powerful Gitea repository operations, including deleting repositories, changing secrets, publishing releases, and creating webhooks. <br>
Mitigation: Use a least-privileged Gitea account or token, verify the target instance and repository, and require deliberate confirmation before mutating or destructive operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ericxliu1990/skills/gitea) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command examples may affect repositories, releases, webhooks, secrets, and other Gitea resources when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
