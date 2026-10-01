## Description:

Helps agents scrape, crawl, map, and search web content through a user-authorized Firecrawl connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use this skill to retrieve website content, discover site URLs, search the web, and configure user-approved Firecrawl automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Non-public URLs, page content, and extraction prompts may be disclosed to Firecrawl.

Mitigation: Confirm the target and obtain user approval before sending non-public URLs or sensitive content.

Risk: Broad crawls, browser actions, or agent prompts may have unintended effects or consume credits.

Mitigation: Review targets, crawl limits, actions, and prompts with the user before execution.

Risk: Hosted functions and triggers can repeatedly forward data to a destination.

Mitigation: Confirm the function, trigger, and destination separately before enabling persistent automation.

## Reference(s):

- [Firecrawl skill release](https://clawhub.ai/byungkyu/skills/firecrawl-api)
- [Firecrawl documentation](https://docs.firecrawl.dev)
- [Maton](https://maton.ai)
- [Maton API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown guidance and commands; Firecrawl results may contain JSON, extracted text, or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, an authorized Firecrawl connection, and user approval before requests.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
