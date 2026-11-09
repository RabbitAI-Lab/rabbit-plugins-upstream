## Description:

Turns a document, topic, or brief into a narrated explainer video, from outline and storyboard through voiceover, generation, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, educators, and teams use this skill to turn documents, topics, or briefs into narrated explainer, training, or courseware videos through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages and options are sent to dLazy's API, and files attached with --files are uploaded to dLazy media storage.

Mitigation: Review attached material and avoid sending sensitive or restricted content unless it is approved for this service.

Risk: The skill relies on a pinned third-party CLI and the security evidence notes that some referenced material could not be resolved.

Mitigation: Review the pinned @dlazy/cli release and relevant service information before use; keep the API key private and rotate it if exposed.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance]

**Output Format:** [Narrated video deliverables with streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based multi-turn sessions; files attached for reference are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.36 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
