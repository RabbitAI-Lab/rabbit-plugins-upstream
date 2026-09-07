## Description:

Researches Fiverr gigs and sellers through the Crawlora API, including keyword search, gig details, pricing packages, ratings, seller profiles, and clean JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Fiverr services, compare gig pricing and packages, and vet sellers by calling documented Crawlora Fiverr endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can redirect the API key to a non-default API base if CRAWLORA_API_BASE is set.

Mitigation: Run with CRAWLORA_API_BASE unset or set only to a trusted Crawlora API base before using the helper.

Risk: The helper can call broader Crawlora paths and methods than the Fiverr-only workflow describes.

Mitigation: Review commands before execution and restrict normal use to the documented Fiverr GET endpoints.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/fiverr-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests should stay within the documented Fiverr endpoints unless reviewed.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
