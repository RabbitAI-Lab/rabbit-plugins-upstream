## Description:

Query Google Play app data through a read-only API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Google Play app metadata, search results, permissions, reviews, data safety details, availability, and related app data through ReplyNodes' read-only API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send public Google Play lookup data to ReplyNodes and may incur metered charges.

Mitigation: Confirm the capabilities response and price before batches, bound pagination and country lists, and stop on payment-gated responses instead of retrying blindly.

Risk: API keys or other credentials could be exposed through prompts, logs, copied commands, screenshots, or reports.

Mitigation: Store the ReplyNodes API key in an environment variable and omit authorization headers, Google credentials, cookies, OAuth tokens, and session data from outputs.

## Reference(s):

- [Google Play Public Data API Skill Page](https://clawhub.ai/replynodes-ai/skills/googleplay-public-data-api)
- [ReplyNodes API Base URL](https://api.replynodes.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides read-only HTTP GET requests and normalized JSON response handling; it does not itself persist files or expose credentials.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
