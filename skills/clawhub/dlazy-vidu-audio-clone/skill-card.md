## Description:

Uses a reference voice to generate spoken audio for new text through Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use an authorized reference voice to generate spoken audio from new text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloned voices could imitate people without their permission.

Mitigation: Use only reference voices you are authorized to clone; review generated speech before sharing.

Risk: Reference recordings are sensitive biometric data uploaded to dLazy's hosted service.

Mitigation: Review dLazy's terms and retention practices before uploading audio; share only necessary recordings.

Risk: Stored API keys may grant continued access to the user's dLazy account.

Mitigation: Prefer per-run keys or revocable organization keys and rotate credentials when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Audio links]

**Output Format:** [JSON response with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before audio is ready.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
