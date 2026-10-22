## Description:

Extracts a video's first frame and audio, analyzes it to create a prompt, and returns a Seedance 2.0 replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers can use the skill to analyze a reference video and obtain a first-frame, audio, and video bundle for a Seedance 2.0 replication workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos and prompts are sent to dLazy for cloud processing, and media may be uploaded to its storage service.

Mitigation: Only submit media and prompts that are appropriate to share with the service; review the service terms before use.

Risk: Requests use dLazy service credits.

Mitigation: Use the dry-run option to preview the request and estimated cost before submitting it.

Risk: The API credential is saved in a local user configuration file and could be exposed if mishandled.

Mitigation: Prefer device-code login over pasting keys into chat, protect the saved credential, and rotate or revoke it if exposed.

## Reference(s):

- [CLI project homepage](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)

## Skill Output:

**Output Type(s):** [JSON, Text, Image files, Audio files, Video files]

**Output Format:** [JSON result with generated media asset URLs; assets can also be saved to a local path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replication bundle includes a first frame, audio, and video.]

## Skill Version(s):

1.3.33 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
