## Description:

Helps agents use the dLazy CLI to align a speaker's lip movements in a video with supplied audio for dubbing and localization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to create lip-synced videos from a source video and audio for dubbing, localization, or virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided video and audio files are uploaded to a hosted service.

Mitigation: Obtain permission for the media and confirm that cloud processing is acceptable before submitting files.

Risk: The dLazy API key is stored locally for CLI authentication.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: The skill's prompt and image examples do not match its video and audio options.

Mitigation: Use the documented video and audio options and check CLI help rather than copying those examples.

Risk: Running a third-party npm CLI executes code outside this skill's documentation.

Mitigation: Review the pinned package before installation; use the on-demand npx option if a global install is unnecessary.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a generated video URL or save the video to a local file.]

## Skill Version(s):

1.3.28 (source: ClawHub release; embedded skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
