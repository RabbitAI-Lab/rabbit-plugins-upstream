## Description:

Replicates a source video by extracting its first frame and audio, using video understanding to create a prompt, and returning a Seedance 2.0 replicate bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create a video-replication bundle from a reference video through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running @dlazy/cli requires trusting third-party npm code.

Mitigation: Review the linked source and npm package before use, and prefer npx or an isolated environment over a privileged global install.

Risk: The skill requires a dLazy API key for authenticated requests.

Mitigation: Use a revocable API key, store it through the CLI auth flow or environment variable, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Reference videos and related media may be uploaded to dLazy-hosted services for processing.

Mitigation: Avoid uploading sensitive media unless the user trusts the service and accepts the data handling path.

Risk: Generated assets can be downloaded to a user-selected local path.

Mitigation: Choose --save destinations deliberately and avoid overwriting important files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous task identifier; --save can download generated assets to a local path.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
