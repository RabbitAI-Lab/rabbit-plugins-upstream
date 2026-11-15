## Description:

ByteDance's Seedance 2.5 video generation skill supports clips up to 30 seconds with up to native 4K output, multimodal references, and first- and last-frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can ask an agent to generate videos from prompts, optionally guided by image, video, or audio references and first or last frames. The skill returns generated media links and task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the advertised video-generation purpose and authentication behavior, with only partial scan coverage; using the pinned CLI also requires providing an API key.

Mitigation: Review the pinned CLI and confirm its authentication flow and referenced materials before installing. Provide an API key only if comfortable, and rotate or revoke it through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands]

**Output Format:** [Generated video URLs and JSON task results, with CLI usage documented in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 4–30 second clips at 480p–2160p with selectable aspect ratios and optional generated audio; image, video, and audio references can be supplied. Results may return asynchronously.]

## Skill Version(s):

1.2.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
