## Description:

Google Forms API integration with managed OAuth for creating forms, adding questions, and retrieving responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Google Forms through Maton-managed OAuth, including reading form metadata and responses, creating forms, and adding or updating questions with user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Maton brokers access to the selected Google Forms account.

Mitigation: Prefer OAuth, review requested Google scopes, connect only the intended account, and revoke unused connections.

Risk: Creating, updating, or deleting forms can modify user data.

Mitigation: Require explicit approval after checking the target form, connection, request payload, and intended effect.

Risk: Multiple linked accounts can make the target connection ambiguous.

Mitigation: Specify the intended Maton connection when more than one Google Forms account is linked.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-forms)
- [Maton](https://maton.ai)
- [Google Forms API Overview](https://developers.google.com/workspace/forms/api/reference/rest)
- [Google Forms Get Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/get)
- [Google Forms Create Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/create)
- [Google Forms Batch Update](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate)
- [Google Forms List Responses](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms.responses/list)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Google Forms API request guidance and Maton CLI commands; write operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
