## Description:

Guides an agent to generate a lip-synced video from an input video and audio using dLazy's hosted sync-lipsync-3 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a speaker's lip movements with supplied audio for dubbing, localization, or virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external npm CLI to run commands.

Mitigation: Review the pinned CLI package and its source before installation.

Risk: Selected video and audio inputs are sent to dLazy cloud services.

Mitigation: Use only media you are authorized to upload and review the service's data handling before submission.

Risk: Authentication may save the dLazy API key locally.

Mitigation: Protect the local credential, avoid sharing it, and rotate or revoke it if exposed.

Risk: Some documentation examples conflict with the listed lip-sync options.

Mitigation: Check `dlazy sync-lipsync-3 -h` for current flags rather than copying the examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands invoke a hosted service that returns a generated video link or an asynchronous task identifier.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
