## Description:

Helps agents inspect Netlify sites, deploys, builds, DNS, and environment variables and perform approved administration through a Maton-managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to review Netlify sites and deployment activity, diagnose builds, and manage approved site settings or automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative actions may alter live sites, DNS, environment variables, or build settings.

Mitigation: Require explicit user confirmation for each write and identify the affected resource before execution.

Risk: Webhooks, triggers, and deployed functions can create persistent actions or forward data.

Mitigation: Confirm every trigger, function deployment, and destination; prefer Maton-hosted destinations.

Risk: Credentials or sensitive API responses may be exposed when handling account access.

Mitigation: Prefer read-only OAuth access, avoid exposing credentials, and limit responses to the fields needed.

## Reference(s):

- [Netlify skill on ClawHub](https://clawhub.ai/byungkyu/skills/netlify-api)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Netlify API documentation](https://open-api.netlify.com/)
- [Netlify build hooks](https://docs.netlify.com/configure-builds/build-hooks/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; writes and automations require explicit user approval.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
