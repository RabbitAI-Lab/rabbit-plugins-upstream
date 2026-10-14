## Description:

Retrieves a Douyin creator's published videos from a profile link, with cursor-based pagination of 20 videos per page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use this skill to retrieve a Douyin account's videos for recent-post review or competitor analysis. The query requires a creator profile link and may incur Qinghu credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or updates of unpinned qhkit and Node tooling may change the host environment.

Mitigation: Review installation first; prefer a sandbox or a preinstalled, pinned qhkit version.

Risk: Configuring a Qinghu API token on the host may leave persistent credentials.

Mitigation: Prefer an environment variable or managed secret over a persistent token configuration.

Risk: Paid video lookups may consume Qinghu credits, especially across multiple pages.

Mitigation: Estimate costs and obtain user approval before paid calls; report actual credits used.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-douyin-creator-videos)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary or tabular data file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video results are paginated; larger result sets may be delivered as a file.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
