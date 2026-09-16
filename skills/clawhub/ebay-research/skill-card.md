## Description:

Researches eBay listings, items, and sellers using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and commerce analysts use this skill to search eBay listings, inspect item details, review seller reputation, and summarize seller shop inventory from public eBay data through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User search terms and request bodies are sent to Crawlora for eBay research.

Mitigation: Avoid sending sensitive private information in search terms or request bodies, and use the skill only when Crawlora is an acceptable third-party API provider.

Risk: The helper requires a Crawlora API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment only; do not hardcode, commit, or pass it in query parameters.

Risk: The skill relies on public eBay listing and seller data returned by an external API.

Mitigation: Use the returned data as research input and respect eBay's terms when acting on public listing or seller information.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/ebay-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized public eBay listing, item, live stream, seller, feedback, and shop data.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
