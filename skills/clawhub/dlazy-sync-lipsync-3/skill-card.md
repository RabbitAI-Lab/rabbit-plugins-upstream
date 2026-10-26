## Description:

Uses fal.ai sync-lipsync v3 to generate a video whose speaker's lip movements match supplied audio, for dubbing, localization, and virtual presenters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers can submit a video and audio track to produce synchronized lip movements for dubbing, localization, or virtual-presenter re-syncing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input video and audio are uploaded to dLazy for processing, and generated media is hosted by the service.

Mitigation: Use media you are comfortable uploading and review the service privacy terms before submitting it.

Risk: API use may incur generation charges.

Mitigation: Review generation charges before running the skill.

Risk: The API key is saved in the local CLI configuration when signing in.

Mitigation: Prefer device login over entering a key in a command, and rotate or revoke the key if needed.

Risk: Some command examples may use incorrect generic fields.

Mitigation: Check `dlazy sync-lipsync-3 -h` and verify the available arguments before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy homepage](https://dlazy.com)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset returned by URL in a JSON result; optionally saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs may return a task ID before the video is ready.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
