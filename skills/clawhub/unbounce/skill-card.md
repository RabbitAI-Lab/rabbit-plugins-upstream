## Description:

Helps agents manage Unbounce landing pages, track leads, and review conversion data through an authorized account connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents use this skill to retrieve and manage Unbounce landing pages and leads, review conversion data, and set up approved account automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a connection can expose Unbounce account data and enable account changes.

Mitigation: Obtain explicit approval for the connection, use only the access needed, and confirm each write with the user.

Risk: Hosted functions, triggers, and destinations can continue acting after setup.

Mitigation: Review and approve each automation, keep its scope narrow, and remove it when no longer needed.

Risk: Manually handling a long-lived API key can expose account credentials.

Mitigation: Prefer the CLI's OAuth login and protected credential storage over copying or exporting an API key.

## Reference(s):

- [Unbounce API reference](https://developer.unbounce.com/api_reference/)
- [Maton](https://maton.ai)
- [Unbounce skill on ClawHub](https://clawhub.ai/byungkyu/skills/unbounce)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Text or Markdown with commands and examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize landing-page, lead, and conversion information or suggest approved account actions.]

## Skill Version(s):

1.2.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
