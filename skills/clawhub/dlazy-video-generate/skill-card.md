## Description:

Helps agents select and run dLazy video models for text-to-video, image-to-video, frame-guided video, and lip-sync tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate or edit videos from prompts and supplied media through dLazy models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Only submit prompts and media you are comfortable sharing with dLazy.

Risk: Using the skill requires a dLazy API key that may be stored locally.

Mitigation: Protect the key and local configuration; rotate or revoke the key if exposed.

Risk: The skill executes a third-party CLI.

Mitigation: Review the CLI before installation; use the pinned npx invocation to avoid a persistent global install.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and commands; generated video URLs are returned in CLI JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video results are hosted by dLazy.]

## Skill Version(s):

1.4.32 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
