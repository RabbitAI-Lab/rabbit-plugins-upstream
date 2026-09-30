## Description:

Helps agents manage CompanyCam projects, photos, documents, and related resources through an authorized connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Contractors and their teams use this skill to review and manage CompanyCam photo documentation, projects, collaborators, and related records. With approval, they can also set up webhooks or automations that act on their CompanyCam account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting CompanyCam grants access to business photo documentation and account resources within the user's authorization.

Mitigation: Confirm the intended connection and limit access to the scopes needed for the task.

Risk: Writes, deletes, webhooks, hosted functions, and persistent triggers can change records or send data to destinations.

Mitigation: Get explicit approval for each intended action and confirm any webhook or trigger destination before creating it.

Risk: API-key fallback requires handling a credential outside the preferred authenticated CLI flow.

Mitigation: Use the authenticated CLI when available and reserve API-key fallback for environments where it cannot be used.

## Reference(s):

- [CompanyCam skill release](https://clawhub.ai/byungkyu/skills/companycam)
- [Maton](https://maton.ai)
- [CompanyCam API documentation](https://docs.companycam.com)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with command examples and API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the user's authorized CompanyCam connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
