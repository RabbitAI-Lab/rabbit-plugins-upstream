## Description:

LinkedIn API integration with managed OAuth for sharing posts, managing profile and organization data, uploading media, and using LinkedIn advertising features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to operate LinkedIn through Maton-managed OAuth, including reading profile or organization information, publishing approved content, uploading media, and managing advertising workflows. It is also used to set up user-approved hosted functions and triggers for LinkedIn-related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad LinkedIn actions can publish content, modify campaigns, change budgets, delete resources, or otherwise affect external accounts.

Mitigation: Default to read and list operations; require explicit user confirmation of the exact target, payload, and effect before any write, delete, campaign, function, trigger, or destination action.

Risk: Credentials or long-lived API keys could be exposed if handled outside the Maton OAuth and credential-store flow.

Mitigation: Prefer OAuth, do not print, export, write, or inspect credentials, and use raw HTTP with a Maton API key only when the CLI cannot be installed.

Risk: Hosted functions, trigger destinations, and event watch execution can create unattended automation or process untrusted event data.

Mitigation: Use only user-authored or user-reviewed handlers, get separate approval for deploys and invocations, avoid --exec unless the handler is reviewed, and keep default function network policy at DENY_ALL.

Risk: LinkedIn media uploads use returned pre-signed upload URLs outside the normal gateway path.

Mitigation: Verify the upload URL was returned by the LinkedIn flow and confirm the specific file before sending sensitive media.

## Reference(s):

- [ClawHub LinkedIn Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Maton Homepage](https://maton.ai)
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/)
- [Share on LinkedIn Guide](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
- [Profile API](https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api)
- [Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [Ad Library API](https://www.linkedin.com/ad-library/api/)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, managed OAuth or a Maton API key, and explicit user approval for writes, deletes, hosted functions, triggers, and destinations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
