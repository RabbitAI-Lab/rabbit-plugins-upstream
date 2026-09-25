## Description:

Quick upload audio to AIOZ Stream API. Create audio objects with default or custom encoding configurations, upload the file, complete the upload, then return the audio link to the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vinhbui3004](https://clawhub.ai/user/vinhbui3004)

### License/Terms of Use:


## Use Case:

External developers and AIOZ Stream users use this skill to create audio objects, upload local audio files, complete transcoding, and retrieve HLS or DASH streaming links through AIOZ Stream API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill sends secret API keys and audio files to a remote host whose AIOZ relationship is not established in the artifacts.

Mitigation: Use the skill only after independently confirming that api-w3stream.attoaioz.cyou is the trusted endpoint for the user's AIOZ Stream account.

Risk: The skill handles stream-public-key and stream-secret-key values in shell commands and HTTP headers.

Mitigation: Use scoped or temporary credentials when available, avoid placing secrets directly in chat transcripts or reusable command history, and rotate any key already used with an endpoint that cannot be verified.

Risk: The upload workflow transmits the selected local audio file to the remote service.

Mitigation: Confirm the exact file path and user authorization before upload, and avoid uploading private or regulated audio unless the destination and account controls are verified.

## Reference(s):

- [AIOZ Stream Audio API Reference](references/api_reference.md)
- [ClawHub skill page](https://clawhub.ai/vinhbui3004/skills/audio-upload-aioz-stream)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces curl-based API call guidance, helper script usage, JSON response handling, and streaming URL retrieval steps.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact metadata lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
