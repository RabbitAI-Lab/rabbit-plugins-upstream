## Description:

Checks any public website's HTTPS setup, TLS certificate expiry and security headers with Corrie's free, read-only checker, and reads uptime, response time and recent checks for sites a user monitors with Corrie. Use when the user asks 'is my site secure', 'check the headers on example.com', 'when does my certificate expire', 'is my site up', 'what was my uptime today', or wants a quick website health or security-header review. No account is needed for the site check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[greg-holman](https://clawhub.ai/user/greg-holman)

### License/Terms of Use:

MIT-0

## Use Case:

Website owners and operators use this skill to review a public site's HTTPS, certificate, and security headers, or to check uptime and recent monitoring results for sites in their Corrie account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A checked URL may contain sensitive path or query data that is sent to Corrie.

Mitigation: Prefer a bare public domain and omit sensitive paths or query parameters.

Risk: A Corrie API token could be exposed in chat or logs.

Mitigation: Keep the token in an environment variable and do not paste it into chat.

## Reference(s):

- [Corrie API documentation](https://corrie.io/resources/api)
- [Corrie OpenAPI specification](https://corrie.io/openapi.json)
- [ClawHub release page](https://clawhub.ai/greg-holman/skills/corrie-site-check)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Concise plain-text or Markdown website health summary with scores, monitoring data, findings, and suggested fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; a site check covers one public page and is not a full security audit.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
