## Description: <br>
Guides an agent through maintaining a configured GitLab project by proposing focused improvement merge requests and closing stale self-authored merge requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to identify useful improvements for the configured GitLab project, open focused merge requests, and close their own stale merge requests when appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to create or close merge requests on a specific GitLab project using GitLab credentials. <br>
Mitigation: Use a least-privilege GITLAB_TOKEN, require explicit approval before creating or closing merge requests, and review proposed changes before execution. <br>
Risk: The skill's public description understates its GitLab repository maintenance behavior. <br>
Mitigation: Treat it as a GitLab repository maintenance workflow rather than a personal-growth aid and verify the target project before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement) <br>
- [Configured GitLab project](https://gitlab.com/xrow-public/helm-openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with possible GitLab CLI shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN as indicated by server-resolved metadata.] <br>

## Skill Version(s): <br>
1.75.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
