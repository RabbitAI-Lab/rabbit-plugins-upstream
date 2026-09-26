## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle (first frame + audio + video).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy video-replicate CLI/API for generating a Seedance 2.0-style replication bundle from a source video, including first frame, audio, and generated video output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI and cloud API, and media files passed to the tool may be uploaded for processing.

Mitigation: Only pass media files intended for upload and review dLazy service terms before use.

Risk: The skill stores or accepts a dLazy API key for authenticated requests.

Mitigation: Protect the API key, prefer per-invocation environment variables or pinned npx use where appropriate, and rotate or revoke the key from dLazy if needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, downloaded files when --save is used, or an asynchronous task identifier when --no-wait is used.]

## Skill Version(s):

1.3.20 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
