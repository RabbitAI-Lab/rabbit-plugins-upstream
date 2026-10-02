## Description:

Helps agents use Brevo to manage contacts and campaigns, send transactional email and SMS, and configure related automations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users can guide an agent to look up Brevo contacts and lists, prepare or send email campaigns and transactional messages, and set up approved workflows using their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Emails, SMS, or campaigns may reach real recipients and cannot always be recalled.

Mitigation: Confirm the audience, sender, content, and intended send with the user before executing it.

Risk: Writes or deletions can change or remove Brevo business data.

Mitigation: Default to read-only operations; verify the connected account, targets, and payload, then obtain explicit approval for each change.

Risk: Hosted functions and triggers can continue performing actions or forwarding data after setup.

Mitigation: Review the function, event scope, destination, and duration with the user; get separate approval and remove unused automations.

Risk: Raw API keys expose longer-lived access if shared or logged.

Mitigation: Prefer CLI/OAuth login and avoid handling raw API keys unless the CLI cannot be used.

## Reference(s):

- [Brevo API documentation](https://developers.brevo.com/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Related API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and user approval for connections and writes.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
