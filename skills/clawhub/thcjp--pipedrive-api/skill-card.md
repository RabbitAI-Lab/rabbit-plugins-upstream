## Description:

Pipedrive API tool for agents to call Maton-hosted Pipedrive endpoints, manage CRM records, and return structured API results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow automation users can use this skill to query and manage Pipedrive CRM data such as deals, people, organizations, and activities through API calls. It is suited to structured CRM automation and status lookup tasks, not tasks that require complex human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and execute authority beyond its CRM API purpose.

Mitigation: Install and run it with only the permissions needed for the specific Pipedrive task, and do not allow unrelated local file or shell-command actions.

Risk: Live CRM write or delete operations could change production Pipedrive records.

Mitigation: Use a least-privilege Maton/Pipedrive credential and require explicit confirmation before production write or delete actions.

Risk: Credential exposure could grant access to CRM data.

Mitigation: Store credentials in environment variables or a secret manager, rotate them when exposed, and avoid printing tokens in logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pipedrive-api)
- [Maton Pipedrive deals endpoint example](https://api.maton.ai/pipedrive/api/v1/deals)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and Python examples plus JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton/Pipedrive credential for live API calls.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
