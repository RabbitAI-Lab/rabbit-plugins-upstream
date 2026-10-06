## Description:

Creates narrated podcast episodes from topics, documents, or slide decks through OnePress and saves the resulting MP3 locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getonepress](https://clawhub.ai/user/getonepress)

### License/Terms of Use:

MIT

## Use Case:

Creators and other users turn topics, documents, or presentations into narrated audio episodes using OnePress, then download the MP3 and receive its local path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Episode requests and uploaded source documents are processed on OnePress servers.

Mitigation: Review sensitive material before submitting it to OnePress.

Risk: Exposing the OnePress API key could allow unauthorized account access.

Mitigation: Use browser-confirmed pairing or a secret store, never paste keys into chat, and revoke unused keys in OnePress settings.

## Reference(s):

- [OnePress](https://www.getonepress.com)
- [OnePress workspace](https://www.getonepress.com/app)
- [ClawHub skill release](https://clawhub.ai/getonepress/skills/onepress-podcast)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Text summary and local MP3 audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the saved MP3 path and conversation title or ID.]

## Skill Version(s):

1.1.1 (source: server release metadata; skill frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
