## Description:

Uploads a local file to OUS object storage and returns the final CDN link after the upload reaches a successful terminal status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatonionlee](https://clawhub.ai/user/fatonionlee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to upload an explicitly chosen local file to OUS object storage using an existing ousToken, globalDomain, and blockSize, then return the resulting URL and upload key only after successful completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading a local file to object storage can expose private or sensitive file contents.

Mitigation: Confirm the exact local file path and intended globalDomain before use, and upload sensitive files only when the transfer is authorized.

Risk: The workflow depends on an ousToken supplied outside the skill, so an incorrect, reused, or unauthorized token can cause upload failure or unintended access.

Mitigation: Use only an authorized token for the intended transfer and avoid providing reusable tokens unless their use is approved.

Risk: A missing, unreadable, or unintended local path can lead to failed transfers or uploading the wrong file.

Mitigation: Verify that the local path exists, is readable, and identifies the intended file before starting single-file or multipart upload.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text containing upload results, command guidance, and failure diagnostics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns url and uploadKey only after successful terminal upload status; may also include taskId, obsTaskId, and md5 when useful for troubleshooting.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
