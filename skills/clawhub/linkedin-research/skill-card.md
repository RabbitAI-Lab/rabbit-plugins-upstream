## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to enrich company records, review product pages, and inspect LinkedIn showcase pages when they already have the relevant LinkedIn ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can call arbitrary Crawlora API paths and HTTP methods with the user's API key, which is broader than the documented LinkedIn-only use case.

Mitigation: Review before installing and restrict usage to the documented GET endpoints for LinkedIn company, product, and showcase lookups unless the helper is narrowed.

Risk: The API key is required for requests and would authorize calls made through the helper.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid committing it, and rotate or revoke it if it may have been exposed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/linkedin-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a LinkedIn company, product, or showcase page ID.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
