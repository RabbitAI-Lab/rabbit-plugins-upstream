## Description:

Helps generate spoken audio in a cloned voice from reference audio and supplied text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate new speech from text using a voice reference they are authorized to provide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloned voices could be used to impersonate people without consent.

Mitigation: Use only reference audio you are authorized to provide; avoid deceptive or impersonating uses.

Risk: Reference audio and prompts are sent to a third-party hosted service.

Mitigation: Review the audio and text before submitting and avoid sending sensitive material without authorization.

Risk: Installing a global CLI or storing an API key can create persistent local exposure.

Mitigation: Prefer on-demand npx execution and a per-run API key when persistence is not needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Audio links]

**Output Format:** [Text instructions and JSON results with generated-media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an immediate media URL.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
