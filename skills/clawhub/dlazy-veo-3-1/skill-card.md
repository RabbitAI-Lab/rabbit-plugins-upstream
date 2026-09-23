## Description:

Generate high-quality cinematic videos with Google Veo 3.1 through the dLazy CLI, supporting text-to-video, image-guided generation, and video extension workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy's Veo 3.1 video generation workflow from prompts, reference images, or source videos. It is useful for creating cinematic generated video assets while keeping authentication, dry runs, async polling, and save-path handling visible to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy for cloud video generation.

Mitigation: Use the skill only for explicit Veo/dLazy requests, avoid sensitive source media unless approved, and prefer dry runs before spending credits.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Use OS-user-restricted configuration, rotate or revoke keys when needed, or provide DLAZY_API_KEY per invocation for temporary credentials.

Risk: Generated output URLs are hosted by dLazy.

Mitigation: Review generated media before sharing and avoid submitting private or regulated content unless dLazy is approved for that use.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted by dLazy; the CLI can save result assets to a local path when requested.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
