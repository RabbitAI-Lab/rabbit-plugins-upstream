## Description:

Researches restaurants and grocery/food delivery via the Crawlora API, including Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search and menus, and Instacart grocery search, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research restaurants, food delivery options, menus, reviews, reservation availability, and grocery search results from supported public platforms through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call API endpoints outside the restaurant, food delivery, and grocery scope.

Mitigation: Constrain use to the documented Yelp, OpenTable, DoorDash, Uber Eats, and Instacart endpoints unless a reviewer explicitly approves broader Crawlora calls.

Risk: Location-scoped searches may involve precise addresses or coordinates.

Mitigation: Use city, neighborhood, postal code, or coarse coordinates when sufficient, and avoid exact home addresses unless the task requires them.

Risk: The Crawlora API key could be exposed if placed in prompts, command history, or files.

Mitigation: Keep CRAWLORA_API_KEY in the environment and do not hardcode, commit, or pass it as a URL query parameter.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment for API calls.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
