## Description:

Researches Fiverr gigs and sellers via the Crawlora API by searching gigs, retrieving gig details, and looking up seller profiles as normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketplace researchers use this skill to find Fiverr gigs, compare package pricing and ratings, and review public seller profile details before making marketplace decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can use arbitrary Crawlora paths, alternate base URLs, and POST bodies with the user's API key.

Mitigation: Review commands before running, keep CRAWLORA_API_BASE unset unless intentionally changed, and prefer only the documented GET endpoints: /fiverr/search, /fiverr/gig/{username}/{slug}, and /fiverr/seller/{username}.

Risk: The skill depends on a Crawlora API key for outbound requests.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid sharing logs that include command environments, and rotate the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/fiverr-research)
- [Crawlora](https://crawlora.net)
- [Fiverr endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Fiverr gig and seller data returned by Crawlora.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
