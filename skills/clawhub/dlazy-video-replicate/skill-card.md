## Description:

Helps agents use dLazy to analyze a source video and prepare a Seedance 2.0 replication bundle with a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request a video replication plan from a reference video, including extracted media and a generated prompt for Seedance 2.0.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media may be uploaded to dLazy's hosted service, and generated outputs are hosted there.

Mitigation: Only submit media and prompts you are authorized to share; review the service's data handling before use.

Risk: Authentication may persist an API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke keys when needed.

Risk: Installing the CLI globally retains a third-party executable on the system.

Mitigation: Prefer the pinned npx invocation if a global installation is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance with CLI commands; the CLI returns JSON containing hosted media URLs or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can download a result to a selected local path.]

## Skill Version(s):

1.3.22 (source: ClawHub release; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
