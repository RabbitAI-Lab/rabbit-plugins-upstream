## Description:

List Azure DevOps projects, repositories, and branches; create pull requests; manage work items; check build status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pals-software](https://clawhub.ai/user/pals-software)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to inspect Azure DevOps project structure, query repositories and pull requests, create pull requests, manage work items, and check build status from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist an Azure DevOps personal access token in a regular configuration file.

Mitigation: Use a least-privilege, short-lived PAT through an environment variable or secret manager, and restrict any configuration file containing credentials to owner-only access.

Risk: The skill includes state-changing Azure DevOps actions such as creating pull requests.

Mitigation: Require explicit human review before creating pull requests or performing other Azure DevOps changes.

## Reference(s):

- [Azure DevOps REST API documentation](https://learn.microsoft.com/en-us/rest/api/azure/devops/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, AZURE_DEVOPS_PAT, and an Azure DevOps organization name.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
