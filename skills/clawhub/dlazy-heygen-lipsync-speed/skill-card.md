## Description:

Uses dLazy's HeyGen Lipsync Speed service to quickly synchronize a video's lip movements with supplied audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate lip-synced video from a video and audio input when fast turnaround matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio inputs are sent to dLazy cloud services.

Mitigation: Confirm the inputs may be shared with dLazy before invoking the CLI.

Risk: Installing the CLI and storing or passing a dLazy API key exposes software and credential handling considerations.

Mitigation: Review the pinned CLI before installation and protect the API key in local configuration or the environment.

Risk: The documented --prompt example does not match the listed lip-sync input options.

Mitigation: Use --video_url and --audio_url, or confirm options with the command help.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI repository (declared in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance and shell commands; CLI results are JSON containing generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later status checks.]

## Skill Version(s):

1.3.30 (source: ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
