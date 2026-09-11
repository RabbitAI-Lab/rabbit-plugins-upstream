## Description:

Researches Old Navy's catalog and its Gap Inc. sibling storefronts Gap, Banana Republic, and Athleta for categories, products, colors and sizes, in-store pickup availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping researchers use this skill to search and browse Old Navy, Gap, Banana Republic, and Athleta catalog data, inspect product details and reviews, and check local pickup availability through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send a Crawlora API key plus shopping search terms, product IDs, and optional ZIP code or coordinates to Crawlora.

Mitigation: Use a dedicated Crawlora key, provide only task-relevant shopping or location values, and avoid including unrelated sensitive information in helper arguments.

Risk: The helper accepts POST bodies even though the documented Old Navy workflow only needs GET requests.

Mitigation: Use the documented GET endpoint patterns unless a reviewer has explicitly approved a POST request for a supported route.

## Reference(s):

- [oldnavy-research on ClawHub](https://clawhub.ai/crawlora-org/skills/oldnavy-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends supported Old Navy, Gap, Banana Republic, and Athleta catalog requests to Crawlora.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
