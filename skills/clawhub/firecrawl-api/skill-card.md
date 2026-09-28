## Description:

Firecrawl API integration with managed authentication for scraping, crawling, mapping, searching, extracting, and browser-based web content workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect a Firecrawl account through Maton and perform approved web scraping, crawling, URL mapping, search, extraction, browser, and agent API workflows from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Firecrawl through Maton can send selected URLs, prompts, and extracted content to Firecrawl.

Mitigation: Install and connect only when the user is comfortable with that data flow, and avoid internal, signed, or authenticated URLs unless they are necessary and explicitly approved.

Risk: Browser actions, hosted functions, triggers, and destinations can spend credits or create ongoing automated data flows.

Mitigation: Require explicit approval before creating connections, writes, hosted functions, triggers, or destinations, and keep routine work to read and list calls first.

Risk: Long-lived Maton API keys or destination credentials can be exposed if copied into commands, logs, headers, or stored automation.

Mitigation: Prefer OAuth and the operating-system credential store, use raw HTTP only when the CLI cannot be installed, and never place Maton or provider credentials in destination headers or logs.

## Reference(s):

- [Firecrawl Skill Page](https://clawhub.ai/byungkyu/skills/firecrawl-api)
- [Firecrawl API Documentation](https://docs.firecrawl.dev/api-reference/v2-introduction)
- [Firecrawl Dashboard](https://firecrawl.dev)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated Firecrawl, function, and trigger calls that require user approval before connection, write, hosted function, trigger, or destination changes.]

## Skill Version(s):

1.2.6 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
