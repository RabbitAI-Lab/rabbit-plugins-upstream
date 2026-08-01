## Description: <br>
Operate assigned GitLab work with owner-verified project access and guarded MR delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to discover assigned GitLab issues and merge requests, verify owner-granted project access, and carry work through guarded branch, CI, review, and merge-request workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad recurring write authority over GitLab repositories with weak human approval boundaries. <br>
Mitigation: Install only for a dedicated, least-privileged GitLab bot account limited to projects where autonomous recurring repository writes are intended. <br>
Risk: Automated pushes, merge-request changes, labels, pipeline actions, forks, new issues, and variable-management workflows can affect repository state. <br>
Mitigation: Require project-level policy for ci.skip pushes, forks, new issues, labels, pipeline actions, merge-request creation, and variable management before deployment. <br>
Risk: Release and variable-management commands may be unnecessary for many deployments. <br>
Mitigation: Review the cron template and disable or remove release and variable-management usage unless it is explicitly needed. <br>


## Reference(s): <br>
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles) <br>
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/) <br>
- [CI Tools Label Component](https://ci-tools.xrow.de/Components/label) <br>
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills) <br>
- [xrow Skills Project](https://gitlab.com/xrow-public/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash, GraphQL, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires glab, jq, and GITLAB_TOKEN; helper scripts emit JSON for active GitLab work and access-gate status.] <br>

## Skill Version(s): <br>
1.78.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
