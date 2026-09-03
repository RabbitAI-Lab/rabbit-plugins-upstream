## Description:

Uploads a specified local file to OUS object storage and returns the final CDN link after the upload reaches a successful terminal state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatonionlee](https://clawhub.ai/user/fatonionlee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to upload an explicitly chosen local file to OUS V2 object storage when they already have an OUS token, global domain, and block size. It guides single-file or multipart upload, status polling, and failure handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could upload an unintended local file, including private data or secrets, if given the wrong path.

Mitigation: Confirm the exact local file path before upload and avoid passing paths that may contain sensitive or private content.

Risk: Uploads could go to the wrong OUS destination if token or domain inputs are stale, reused, or copied from the wrong response.

Mitigation: Confirm the OUS token source, global domain, and block size before use, and stop on token errors instead of retrying blindly.

Risk: A failed or incomplete upload could be mistaken for success if intermediate response fields are treated as final.

Mitigation: Return URL and upload key only after the status endpoint reports the successful terminal state.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, text]

**Output Format:** [Markdown instructions with endpoint, upload, polling, and failure-handling rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the final URL and upload key only after successful terminal upload status.]

## Skill Version(s):

1.0.5 (source: server release metadata and auto changelog; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
