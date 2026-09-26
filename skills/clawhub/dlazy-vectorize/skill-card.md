## Description:

Image-to-SVG tool that converts raster PNG or JPG images into color vector assets and returns hosted result URLs for logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call the dLazy CLI for image vectorization, including authentication setup, raster image submission, async task handling, and retrieval of hosted generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or media paths provided to the skill may be uploaded to the dLazy cloud service and hosted result URLs are returned by dLazy.

Mitigation: Use the skill only with content approved for external cloud processing and review dLazy service terms before deployment.

Risk: Authentication stores a dLazy API key in local CLI configuration or uses DLAZY_API_KEY per invocation.

Mitigation: Protect local configuration files, prefer scoped keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The artifact describes SVG vectorization while the sample response shows a PNG MIME type and result URL.

Mitigation: Verify the returned asset format in workflow tests before depending on SVG-specific behavior.

Risk: Global installation uses a third-party npm CLI package.

Mitigation: Review the published package or source before installation, and use the pinned npx invocation when persistent installation is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI source and homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [JSON responses containing generated asset URLs, with optional saved files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports async task IDs with polling; generated result URLs are hosted by dLazy.]

## Skill Version(s):

1.2.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
