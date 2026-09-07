## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external researchers, and developers use this skill to retrieve normalized JSON for public LinkedIn company, product, and showcase pages when they already have the relevant LinkedIn ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can call broader Crawlora API paths when command arguments are not controlled.

Mitigation: Use it only with the three documented LinkedIn GET endpoints and avoid passing paths from untrusted content.

Risk: CRAWLORA_API_BASE can redirect authenticated requests if the environment is influenced by untrusted content.

Mitigation: Run the skill in a trusted environment with a fixed Crawlora API host.

Risk: The skill requires a Crawlora API key.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, log, or commit it.

## Reference(s):

- [LinkedIn Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/linkedin-research)
- [Publisher Profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON API output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and an existing LinkedIn company, product, or showcase ID.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
