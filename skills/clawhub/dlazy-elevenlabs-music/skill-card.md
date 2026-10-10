## Description:

Generates 10–300 seconds of original music from a text prompt using ElevenLabs music_v1 for background music, ads, and short videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short music tracks for background audio, advertising, and videos from natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key is stored locally for CLI authentication.

Mitigation: Protect the local CLI configuration and rotate or revoke the key if exposed.

Risk: Prompts and any explicitly supplied media files are sent to dLazy's cloud service.

Mitigation: Only submit content approved for cloud processing; review the selected files before running the command.

Risk: Using the CLI requires installing or executing the pinned third-party npm package.

Mitigation: Review the package before use; choose the documented pinned npx invocation to avoid a global install.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Audio links, Shell commands, Configuration guidance]

**Output Format:** [Markdown with generated audio links; CLI responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task ID or save generated audio locally.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
