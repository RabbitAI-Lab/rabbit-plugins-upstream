## Description:

Checks xAI OAuth usage, remaining quota, and reset time in read-only mode using an existing Hermes xai-oauth credential.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hirorylabo](https://clawhub.ai/user/hirorylabo)

### License/Terms of Use:

MIT-0

## Use Case:

Hermes Agent users and operators use this skill to check xAI or Grok weekly quota status, remaining allowance, and reset timing without changing credentials or performing billing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the existing Hermes xai-oauth access token and sends it to the xAI Grok billing endpoint for a quota check.

Mitigation: Run it only after user approval for a read-only quota request, and do not use it for reauthentication, credential changes, or billing actions.

Risk: Quota results may be mistaken for a model-specific limit or treated as recovered before the billing period ends.

Mitigation: Report the value as weekly xAI OAuth quota status, use the returned reset time as authoritative, and treat remaining-time values as approximate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hirorylabo/skills/xai-oauth-usage)
- [xAI billing endpoint used by the skill](https://cli-chat-proxy.grok.com/v1/billing?format=credits)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Human-readable text or sanitized JSON, usually summarized in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports usage percentage, remaining quota, reset time, approximate remaining time, and product usage; token values and raw API responses are not output.]

## Skill Version(s):

1.2.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
