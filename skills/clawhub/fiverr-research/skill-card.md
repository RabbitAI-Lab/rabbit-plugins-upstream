## Description:

Researches Fiverr gigs and sellers via the Crawlora API by searching gigs by keyword, retrieving full gig details, and looking up seller profiles as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and sourcing teams use this skill to find Fiverr gigs, compare pricing and packages, and review public seller profile data before making marketplace decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora endpoints and send arbitrary request bodies, beyond the documented Fiverr research endpoints.

Mitigation: Install only when agents may use the Crawlora API key for this workflow, and narrow usage to the documented Fiverr endpoints before broad deployment.

Risk: Fiverr research queries and marketplace terms are sent to Crawlora.

Mitigation: Avoid sending sensitive prompts, confidential sourcing strategies, or business research terms unless that sharing is approved.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/fiverr-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Fiverr gig and seller data through Crawlora.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
