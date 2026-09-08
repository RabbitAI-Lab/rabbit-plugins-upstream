## Description:

Compare restaurant menu breadth, matched dishes, bundles, and location-specific prices with the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, operators, and developers use this skill to compare restaurant branch menus, matched dishes, bundles, availability, and location-specific prices across direct, pickup, and delivery sources in a defined market.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can send the Crawlora API key to an endpoint selected through the environment.

Mitigation: Use the skill only in a controlled environment, set CRAWLORA_API_KEY deliberately, and leave CRAWLORA_API_BASE unset unless it points to the trusted Crawlora API base.

Risk: The API helper is broader than the restaurant-menu workflow described by the skill.

Mitigation: Keep requests limited to the documented restaurant-menu endpoints and avoid untrusted wrappers or CI environments that can alter execution.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/restaurant-menu-benchmarking)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown tables and concise narrative, with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes collection timestamps, source IDs or URLs, match confidence, coverage summaries, missing sources, and pricing hypotheses.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
