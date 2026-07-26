## Description: <br>
Detects shared stack membership and iterates a command across all PRs in base-to-tip order. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill when a review or fix command needs to operate across a stack of dependent pull requests while preserving each pull request's normal workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to inspect pull request relationships and post a consolidated comment on the root pull request. <br>
Mitigation: Use it in repositories where the agent is authorized to use git and GitHub or GitLab CLI access, and review automated or public comments before posting when approval is required. <br>
Risk: Automatic stack detection could expand a single-pull-request workflow into multiple pull requests. <br>
Mitigation: Prefer an explicit --stack workflow, and require user confirmation before running stack mode when stack membership is auto-detected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-mode) <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with shell command examples and summary comment templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces stack membership guidance, progress tracking markers, failure handling notes, and a root pull request summary format.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter states 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
