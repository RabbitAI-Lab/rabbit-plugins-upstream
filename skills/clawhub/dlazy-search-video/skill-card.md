## Description:

Searches for stock videos through the dLazy service and returns video links and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use this skill to find stock video footage by keyword and review video links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, parameters and API key usage go to dLazy infrastructure rather than directly to Pixabay.

Mitigation: Review what you submit and treat the service as a third-party data recipient.

Risk: Local media paths supplied to the CLI may cause files to be uploaded; login may save an API key locally.

Mitigation: Avoid local file paths unless uploading is intended, and use a per-run DLAZY_API_KEY if you do not want a saved credential.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (metadata link; not verified release provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summary of video links and metadata; the CLI returns JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include video URLs, metadata, and an asynchronous task identifier.]

## Skill Version(s):

1.3.28 (source: ClawHub release; bundled skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
