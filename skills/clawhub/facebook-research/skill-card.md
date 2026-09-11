## Description:

Searches Facebook Marketplace listings and looks up public Facebook Page details through the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users can use this skill to collect public Facebook Marketplace listing data or public Facebook Page profile details through Crawlora instead of scraping Facebook directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send undocumented POST requests to broad Crawlora Facebook API paths using the user's Crawlora API key.

Mitigation: Review or restrict the helper to the documented read-only GET endpoints before use if that API access is broader than intended.

Risk: The skill requires a Crawlora API key and sends Facebook-related requests to Crawlora.

Mitigation: Provide the key only through CRAWLORA_API_KEY and use an account or key whose permissions and credit exposure are acceptable for the task.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/facebook-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands that return raw JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
