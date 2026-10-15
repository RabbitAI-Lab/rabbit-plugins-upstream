## Description:

Retrieves videos from a WeChat Channels collection by topic ID using Qinghu's qhkit, with cursor-based pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, analysts, and other users can retrieve and organize videos from a specified WeChat Channels collection, including additional pages of results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Qinghu lookups spend credits, including possible charges for failed service calls or additional pages.

Mitigation: Check the current estimate, obtain user consent before paid calls, and agree on additional calls before exceeding the session's limit.

Risk: The skill directs agents to install or upgrade qhkit and may modify the local Node environment or shell PATH.

Mitigation: Review installation and PATH changes first; prefer a pinned, preinstalled qhkit in a managed or disposable environment.

Risk: Local qhkit configuration can persist an API token on the host.

Mitigation: Inject the token temporarily instead of storing it in local configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-collection-videos)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Markdown summary and optional tabular file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large results may be delivered as a file; paid calls report Qinghu credit usage.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
