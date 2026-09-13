## Description:

Researches Pinterest profiles, boards, pins, ideas categories, and search results via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to look up public Pinterest profiles, boards, pins, category feeds, and keyword search results for content research, competitor audits, and trend scouting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Crawlora requests may go beyond the documented read-only Pinterest lookups if the helper is used with a valuable or paid API key before review.

Mitigation: Review before installation, prefer a limited or low-value API key, and tighten the helper to GET-only documented routes with segment-aware path validation.

Risk: The Crawlora API key could be exposed if users hardcode it, pass it in URLs, or commit it with project files.

Mitigation: Set the key only through CRAWLORA_API_KEY, avoid logging command environments, and rotate the key if it is exposed.

## Reference(s):

- [Pinterest endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/pinterest-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Pinterest data returned by Crawlora.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
