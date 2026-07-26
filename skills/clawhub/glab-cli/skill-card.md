## Description: <br>
Interact with GitLab using the `glab` CLI. Use when Claude needs to work with GitLab merge requests, CI/CD pipelines, issues, releases, or make API requests. Supports gitlab.com and self-hosted instances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[portavion](https://clawhub.ai/user/portavion) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to work with GitLab merge requests, CI/CD pipelines, issues, releases, CI/CD variables, and GitLab REST or GraphQL API requests through the authenticated `glab` CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use an agent's authenticated GitLab CLI context for broad write and API operations. <br>
Mitigation: Use a least-privilege GitLab token and require explicit approval before merges, approvals, pipeline retries, issue or release creation, CI/CD variable changes, non-GET API calls, or commands against private or production projects. <br>
Risk: The security evidence reports broad GitLab write and API power without clear safety guardrails. <br>
Mitigation: Review generated `glab` commands before execution and restrict operations to intended repositories and environments. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce GitLab CLI commands that return JSON or pipeline, issue, merge request, release, and API results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
