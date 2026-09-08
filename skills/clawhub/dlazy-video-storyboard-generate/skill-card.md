## Description:

Converts storyboard details into a canvas-ready video generation pipeline with shared source audio, a shared scene image, cloned dialogue audio, and per-storyboard video nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative workflow users use this skill to transform storyboard context into structured video-generation canvas elements. It helps lay out audio, image, and video nodes for each storyboard segment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags the release as suspicious because it installs and runs an external dLazy npm CLI.

Mitigation: Use a contained, non-global setup where possible, verify the package and source before use, and require explicit confirmation before running generation commands.

Risk: The skill stores or uses a dLazy API key and sends prompts or referenced media to dLazy services.

Mitigation: Avoid sensitive prompts or media, prefer per-session environment variables when practical, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Terminal generation instructions can turn user text into shell command arguments.

Mitigation: Avoid building shell command strings from unescaped user text and execute only one confirmed generation command at a time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON pipeline snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; generated media URLs are hosted by dLazy services.]

## Skill Version(s):

1.2.12 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
