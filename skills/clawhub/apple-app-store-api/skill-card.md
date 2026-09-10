## Description:

Search the Apple App Store, read a full app listing by App Store id or bundle id, and pull user reviews as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and app growth teams use this skill to search App Store listings, inspect app metadata, compare publisher catalogues, and collect review data across Apple storefronts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and uses paid or free credits for requests.

Mitigation: Keep SCAVIO_API_KEY out of source control, store it in an environment or secret manager, and monitor credit usage before running bulk collection.

Risk: Optional SDK installation can add dependencies to the active environment.

Mitigation: Use the direct HTTPS examples when possible, or install optional SDKs in an isolated project environment.

## Reference(s):

- [Scavio App Store Search Documentation](https://scavio.dev/docs/app-store-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=apple-app-store-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/apple-app-store-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces structured App Store search, listing, and review data through Scavio API calls; requires SCAVIO_API_KEY.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
