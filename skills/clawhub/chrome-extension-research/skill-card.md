## Description:

Compare Chrome extensions using Crawlora's live store listings and stored adoption, publisher, permission, and privacy history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and product teams use this skill to compare Chrome extension candidates using live and stored store metadata, permission and privacy disclosures, historical changes, and review samples while keeping store evidence separate from code or runtime safety conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chrome extension search terms, extension IDs, and related research queries are sent to Crawlora with a Crawlora API key.

Mitigation: Keep the API key in the environment, avoid including secrets or private local file contents in request bodies, and install only when this data sharing is acceptable.

Risk: Store metadata, privacy disclosures, permissions, ratings, and reviews can support research but do not prove an extension is safe.

Mitigation: Treat store data as research evidence, distinguish observations from developer claims, and require code or runtime review before making safety conclusions.

## Reference(s):

- [Chrome extension research endpoint reference](reference/endpoints.md)
- [Chrome permission definitions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/chrome-extension-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown comparison with inline shell commands and evidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON from Crawlora API calls when useful for extension research.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
