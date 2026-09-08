## Description:

Researches public BBC, CNN, and Guardian news through the Crawlora API — headlines, article text, live-story updates, search, and topic archives — returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to search and read public BBC, CNN, and Guardian coverage as normalized JSON through Crawlora-backed endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can make arbitrary authenticated Crawlora API requests beyond the BBC, CNN, and Guardian endpoints documented for this skill.

Mitigation: Review commands before execution and prefer a version that allowlists only the documented news endpoints.

Risk: CRAWLORA_API_BASE can redirect the Crawlora API key to an overridden API origin.

Mitigation: Run the skill only in trusted environments, avoid untrusted configuration for CRAWLORA_API_BASE, and prefer hardcoded or validated API origins.

Risk: Using a broad Crawlora credential may expose more access than this news workflow requires.

Mitigation: Use a low-privilege Crawlora key when available and rotate the key if it may have been exposed.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public news metadata, headlines, article bodies, live-story updates, search results, and topic archives.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
