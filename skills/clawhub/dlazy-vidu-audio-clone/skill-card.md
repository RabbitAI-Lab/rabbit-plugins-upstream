## Description:

Clone a voice from reference audio and generate spoken audio from new text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to submit reference audio and text to a voice cloning service, then receive generated speech results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports that observed login-only behavior does not match the advertised voice cloning workflow, and its scan was partial.

Mitigation: Review the CLI installation details and behavior before use, and verify the advertised workflow before providing credentials.

Risk: The documented CLI sends prompts and supplied media to dLazy hosted services and stores an API key in local CLI configuration when using its login flow.

Mitigation: Share only prompts and recordings you are authorized to send to the service; protect the API key and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy service homepage (skill metadata)](https://dlazy.com)
- [CLI project link (skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Generated media URLs]

**Output Format:** [Markdown instructions and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return hosted output URLs; asynchronous runs can initially return a task ID.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
