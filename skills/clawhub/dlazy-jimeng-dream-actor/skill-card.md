## Description:

Converts a static character image into an action video with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create action videos from a character image by supplying a prompt and optional reference media to Jimeng Dream Actor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input media are sent to dLazy for cloud generation, and local media files may be uploaded to its media storage.

Mitigation: Only submit media you are comfortable uploading, and review the provider's terms before use.

Risk: The CLI stores the API key in a local user configuration file.

Mitigation: Protect the local configuration and rotate or revoke the key from the dashboard if needed.

Risk: Video generation may consume credits or incur costs.

Mitigation: Check the cost estimate and available credits before starting generation.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON result envelope with generated media URLs or asynchronous task status; optionally a media file saved to a local path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are hosted by dLazy and can be downloaded locally.]

## Skill Version(s):

1.3.33 (source: server-resolved release; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
