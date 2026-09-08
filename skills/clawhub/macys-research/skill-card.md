## Description:

Looks up a Macy's product's full detail and customer reviews by its numeric productId, and pulls Macy's own search-box typeahead suggestions using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Macy's product details, reviews, rating summaries, color variants, pricing, and typeahead suggestions when they already have a numeric Macy's productId or a partial search-box query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send authenticated Crawlora requests to arbitrary paths and an overridden API base, which is broader than the Macy's-only behavior described by the skill.

Mitigation: Review before installing, run in a trusted environment, and prefer a version that restricts requests to the three Macy's endpoints and validates the API host before sending credentials.

## Reference(s):

- [Macy's endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/macys-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Crawlora API key from CRAWLORA_API_KEY and returns public Macy's product, review, and typeahead data.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
