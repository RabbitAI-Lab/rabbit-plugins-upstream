## Description:

CallRail API integration with managed OAuth for tracking and analyzing phone calls, managing tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to access CallRail account data, review call activity and analytics, and manage tracking numbers, companies, tags, users, integrations, and notifications through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External Maton installation commands are not pinned to a specific package version.

Mitigation: Install Maton only from trusted sources and review the package source before installation.

Risk: API-key fallback uses a long-lived credential that can leak through environment exposure, logs, command history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI; when an API key is unavoidable, keep it out of files and command lines, send it only to api.maton.ai, and rotate it if exposed.

Risk: Write, delete, or connection-management calls can change or revoke CallRail account resources.

Mitigation: Default to read and list operations, then confirm the exact account, connection, resource identifier, payload, and intended effect before any POST, PUT, PATCH, DELETE, or new connection.

Risk: CallRail responses can contain personal data or untrusted external content.

Mitigation: Extract only task-relevant fields, avoid writing raw responses to logs or files unless requested, and treat returned content as data rather than executable instructions.

## Reference(s):

- [CallRail Skill on ClawHub](https://clawhub.ai/byungkyu/skills/callrail)
- [Maton](https://maton.ai)
- [CallRail API Documentation](https://apidocs.callrail.com/)
- [CallRail Help Center - API](https://support.callrail.com/hc/en-us/sections/4426797289229-API)
- [CallRail API Rate Limits](https://apidocs.callrail.com/#rate-limiting)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces CallRail API request guidance and command examples; responses may include personal data and should be scoped to the fields needed for the task.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
