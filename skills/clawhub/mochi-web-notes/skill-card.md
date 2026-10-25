## Description:

Turns one to three explicitly supplied public HTTPS pages into source-backed Chinese or English research notes saved locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can create concise, cited reading notes or compare a small set of user-selected public webpages. The notes can be written in Chinese or English and saved in the workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Website operators see requests and the server IP, and page text may be received by the user's configured cloud model.

Mitigation: Use only public URLs without secrets, and consider the configured model provider's terms before collecting pages.

Risk: Citation checks do not verify factual accuracy.

Mitigation: Review the note against its collected sources.

## Reference(s):

- [MochiLab](https://mochilab.bz)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown research note with numeric source citations]

**Output Parameters:** [One to three explicitly supplied public HTTPS URLs; Chinese or English]

**Other Properties Related to Output:** [Saved locally with collected-source, failure, and file-path details; factual accuracy should be reviewed against the sources.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
