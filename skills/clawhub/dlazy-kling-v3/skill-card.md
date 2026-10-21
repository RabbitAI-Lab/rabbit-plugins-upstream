## Description:

Guides agents in generating Kling V3 videos from text prompts or reference images through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through text-to-video or image-to-video generation with Kling V3 via dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Only submit content you are comfortable sharing with dLazy; review selected files before invoking the CLI.

Risk: Using a third-party CLI may install software globally or store an API key locally.

Mitigation: Review the CLI source before sensitive use; prefer the pinned on-demand npx command and a per-invocation API key when avoiding global installs or stored credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source (declared in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for video generation; generated media is hosted by dLazy and may be downloaded separately.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
