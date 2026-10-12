## Description:

Helps agents use dLazy to analyze a source video and produce a Seedance 2.0 replication bundle with a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in preparing a video replication request from a reference video through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected media may be sent to the third-party dLazy cloud service.

Mitigation: Avoid sending sensitive media or prompts unless sharing them with dLazy is acceptable.

Risk: The dLazy API key may be stored locally, and installing the CLI introduces a dependency on an external npm package.

Mitigation: Use DLAZY_API_KEY or the on-demand npx option when persistence is undesirable, and review the pinned package before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text or Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results may include generated media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.28 (source: server-resolved release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
