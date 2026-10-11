## Description:

Queries WeChat Channels video details using a video ID or share link through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and analysts query details for a specific WeChat Channels video using its object ID, export ID, or share link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic setup or upgrades may change Node/npm tooling, install unpinned packages, or persist PATH changes.

Mitigation: Review installation steps, preinstall and pin trusted qhkit versions, and avoid persistent PATH changes unless needed.

Risk: Configuring an API token changes local credential settings.

Mitigation: Review credential setup before providing a Qinghu API token.

Risk: Video-detail requests consume paid Qinghu credits.

Mitigation: Check the current credit estimate and obtain consent before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-video-data)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise natural-language summary with video details and optional file for large results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid queries require user consent and disclosure of credits used.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
