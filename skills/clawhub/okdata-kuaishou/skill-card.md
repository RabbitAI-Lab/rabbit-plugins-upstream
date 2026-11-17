## Description:

Provides public Kuaishou video, comment, account, and trending data through okdata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data analysts use it to retrieve public Kuaishou videos, comments, account details, and trending topics for research and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use an external API service, and the security scan was partial, so its evidence is incomplete.

Mitigation: Review the API service and the information sent in requests before use; check endpoint prices and limit calls to those needed.

## Reference(s):

- [Kuaishou API documentation](https://okdata.online/apis/kuaishou/?src=skill-okdata-kuaishou)
- [okdata agent setup guide](https://okdata.online/agents.md)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Text containing Kuaishou data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One page per request; each additional page requires another API call.]

## Skill Version(s):

0.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
