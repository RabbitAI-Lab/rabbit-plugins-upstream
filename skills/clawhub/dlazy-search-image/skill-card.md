## Description:

Searches for image assets through the dLazy CLI and returns image URLs and metadata for design references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users search for reference images, backgrounds, and design assets by keyword and review returned image URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A search uses the dLazy hosted service and requires an API key stored locally when using the CLI login flow.

Mitigation: Review the service before use, protect the local API key, and revoke or rotate it if exposed.

Risk: Local media paths passed to supported commands may upload files to dLazy.

Mitigation: Do not supply local media paths unless the upload is intended and approved.

Risk: The CLI has broader account and media capabilities than a direct Pixabay-only search.

Mitigation: Review the CLI and use a sandboxed or one-off invocation when only image search is needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON with image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a returned asset locally when requested.]

## Skill Version(s):

1.3.23 (source: server release metadata; bundled instructions list 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
