## Description:

Brave Search API integration with managed authentication for web, image, news, video, local, suggestion, spellcheck, and summarizer searches through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Brave Search through a Maton-authenticated connection, inspect returned results, and optionally configure approved hosted automation or scheduled checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton API keys and OAuth-backed credentials can be exposed if printed, persisted, passed on a command line, or embedded in trigger destinations.

Mitigation: Prefer OAuth-backed CLI use, never inspect or log credential values, use raw API keys only when the CLI cannot be installed, and send Maton credentials only to api.maton.ai.

Risk: Functions, triggers, destinations, local --exec handlers, and raw API keys can turn a one-off search workflow into persistent automation or data egress.

Mitigation: Use normal Brave Search API calls by default; require explicit approval for each automation step, review the exact data flow and destination, scope triggers narrowly, and prefer DENY_ALL network policy for hosted functions.

Risk: Location headers can disclose precise physical location to Brave Search.

Mitigation: Send location headers only when the user supplied or approved the location for a location-dependent query, prefer coarse location values, and do not log or reuse location headers silently.

Risk: Search results, trigger payloads, and other third-party content may contain untrusted text or sensitive data.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, extract only the fields needed for the task, and avoid logging raw responses.

## Reference(s):

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Brave Search API Dashboard](https://api-dashboard.search.brave.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/brave-search-api)
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

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are JSON; authenticated calls require a Maton account and network access.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
