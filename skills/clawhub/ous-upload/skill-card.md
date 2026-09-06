## Description:

Uploads an existing local file to OUS object storage and returns the final CDN URL after the upload reaches a successful terminal status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatonionlee](https://clawhub.ai/user/fatonionlee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to upload user-approved local files to an OUS object-storage service when an ousToken, globalDomain, and blockSize have already been obtained.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads local files to an external OUS object-storage service.

Mitigation: Verify the local file path, destination domain, and token before invoking it, and do not use it on secrets, credentials, private user data, or unrelated files without explicit approval.

Risk: Upload tokens and service parameters must be supplied by the caller and may be incorrect, expired, or reused.

Mitigation: Confirm ousToken, globalDomain, and blockSize are current and intended for the target upload before starting the workflow.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, shell commands, API calls, guidance]

**Output Format:** [Markdown with returned upload URL, upload key, status details, and troubleshooting information when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns url and uploadKey only after confirmed successful upload status; may include taskId, obsTaskId, and md5 for troubleshooting.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
