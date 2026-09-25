## Description:

HeyGen Lipsync Speed helps agents run dLazy's hosted HeyGen lip-sync speed model to generate fast lip-sync results from supplied video and audio inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's cloud lip-sync workflow for quickly synchronizing a video's mouth movement with a supplied audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the supplied video, audio, prompts, and parameters to dLazy's hosted API and may upload local media files to dLazy storage.

Mitigation: Use it only with files and parameters approved for the dLazy service, and confirm users are comfortable with cloud processing before execution.

Risk: The workflow requires a dLazy API key and use of the dLazy CLI package.

Mitigation: Install the pinned CLI only after trusting the package, store credentials with dlazy login or dlazy auth set, and rotate or revoke keys when needed.

Risk: The artifact contains documentation mistakes, including an outdated prompt-style example that does not match the documented video_url and audio_url options.

Mitigation: Prefer dlazy heygen-lipsync-speed -h and the documented video_url and audio_url flags when forming commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated asset URLs or an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
