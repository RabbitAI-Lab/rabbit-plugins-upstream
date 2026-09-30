## Description:

Helps agents generate videos from text, reference media, or first and last frames using dLazy's Seedance 2.0 Fast service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request fast video generation with text prompts, reference images, videos, or audio, or specified first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external dLazy CLI runs third-party software on the user's machine.

Mitigation: Review the pinned @dlazy/cli package before global installation; use npx for on-demand execution if a persistent binary is not wanted.

Risk: Reference media supplied as local files is uploaded to dLazy's hosted service.

Mitigation: Only submit media that the user is comfortable uploading to dLazy.

Risk: Logging in can save the dLazy API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run access if the user does not want the key stored locally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text guidance and JSON CLI responses with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of an immediate media URL.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
