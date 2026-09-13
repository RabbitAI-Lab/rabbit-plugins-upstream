## Description:

Google Meet API integration with managed OAuth for creating meeting spaces, listing conference records, and managing meeting participants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform user-approved Google Meet API work through Maton, including reading conference records, creating meeting spaces, and retrieving participant, recording, transcript, and note data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the Maton Google Meet connection grants access to Google Meet data available to the connected account.

Mitigation: Use OAuth, choose least-privilege scopes when offered, confirm connection creation with the user, and revoke unused connections when no longer needed.

Risk: Write calls, function deployments, trigger destinations, or event watch --exec can create persistent automation or data forwarding.

Mitigation: Confirm every write and automation action separately, keep trigger destinations on Maton-controlled hosts unless another host is explicitly approved, and avoid --exec unless the handler was written or reviewed for that purpose.

Risk: Raw HTTP API-key mode can expose a long-lived credential if mishandled.

Mitigation: Prefer CLI OAuth. When raw HTTP is required, keep the key out of command lines and logs, store it only in the process environment, and rotate it if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-meet)
- [Maton Homepage](https://maton.ai)
- [Google Meet API Overview](https://developers.google.com/meet/api/reference/rest)
- [Google Meet Spaces API](https://developers.google.com/meet/api/reference/rest/v2/spaces)
- [Google Meet Conference Records API](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit Maton CLI or API calls that require OAuth or API-key authentication and explicit user approval before writes or automation.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
