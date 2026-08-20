## Description:

Researches Pinterest profiles, boards, pins, ideas categories, and search results via the Crawlora API, returning clean JSON for public Pinterest research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Pinterest profiles, boards, pins, idea categories, and keyword search results through the Crawlora API. It supports competitor board audits, content-idea research, trend scouting, and brand or product mention sweeps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora API paths and methods beyond the advertised Pinterest scope, potentially using the configured Crawlora API key for unrelated requests.

Mitigation: Review proposed commands before execution, restrict use to documented /pinterest/* workflows, and provide CRAWLORA_API_KEY only in trusted agent sessions.

Risk: The skill works with public Pinterest data and depends on a third-party API service.

Mitigation: Use it only for public profiles, boards, pins, and category feeds; respect Pinterest terms and the Crawlora account's usage limits.

## Reference(s):

- [Pinterest Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/pinterest-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; documented workflows use public Pinterest data and GET endpoints.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
