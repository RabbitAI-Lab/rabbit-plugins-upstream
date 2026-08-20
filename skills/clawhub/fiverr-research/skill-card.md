## Description:

Researches Fiverr gigs and sellers via the Crawlora API - search gigs by keyword, pull a gig's full detail (packages, pricing tiers, rating, seller summary), and look up a seller's profile - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to search Fiverr gigs, compare package pricing and delivery details, and evaluate public seller profiles before recommending or selecting freelance services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths and methods beyond the Fiverr endpoints described by the skill.

Mitigation: Restrict agent use to the documented Fiverr endpoints or modify the helper to allowlist only /fiverr/search, /fiverr/gig/{username}/{slug}, and /fiverr/seller/{username}.

Risk: The skill requires a Crawlora API key for API calls.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid hardcoding or committing it, and review agent-issued API calls before use.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/fiverr-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns normalized public Fiverr gig and seller data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
