## Description:

Turns a document, topic, or brief into a narrated explainer video through outlining, storyboarding, voiceover, video assembly, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing training, courseware, reports, or explainers can use this skill to turn a document, topic, or brief into a narrated video. It guides an agent through the dLazy file-to-video workflow and project-based follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Files attached for video creation are uploaded to dLazy media storage and referenced by URL.

Mitigation: Attach only documents you are permitted to share, and confirm the intended project before uploading.

Risk: The CLI uses an organization API key saved in local configuration or supplied per invocation.

Mitigation: Protect the key and rotate or revoke it when it is no longer needed.

Risk: Hosted video generation may consume service credits.

Mitigation: Consider the credit cost before starting a generation.

Risk: The external CLI implementation and hosted service were not audited in this review.

Mitigation: Review the CLI and service terms before using sensitive documents or relying on the service for important work.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Explainer videos, Text, Shell commands, Configuration instructions]

**Output Format:** [Narrated video deliverable with streamed text responses and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the hosted file-to-video workflow; files supplied with --files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.34 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
