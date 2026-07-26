## Description: <br>
Manage GitLab repositories, merge requests, and issues via API. Use for tasks like creating repos, reviewing code in MRs, or tracking issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jorgermp](https://clawhub.ai/user/jorgermp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to automate common GitLab project, merge request, and issue workflows from an agent session. It is useful when an agent needs to create repositories, list merge requests, comment on reviews, or open issues through the GitLab API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a GitLab token to create or modify repositories, merge request comments, and issues. <br>
Mitigation: Use the narrowest GitLab token scopes possible and review mutating actions before they run. <br>
Risk: Using the skill on sensitive private projects may expose or change project information if the token is overprivileged or misused. <br>
Mitigation: Run it only on authorized projects and avoid sensitive private repositories unless the token and action are explicitly approved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jorgermp/skills/gitlab-manager) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/jorgermp) <br>
- [GitLab REST API v4](https://gitlab.com/api/v4) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Text, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with command examples; script output is status text or JSON from GitLab API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a GITLAB_TOKEN environment variable with permissions appropriate to the requested GitLab action.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
