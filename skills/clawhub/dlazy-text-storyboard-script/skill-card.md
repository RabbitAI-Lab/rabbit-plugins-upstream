## Description:

Generates detailed short-video storyboard scripts from user themes, outlines, or structured copy while preserving spoken-script text verbatim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and production teams use this skill to turn themes, outlines, or structured copy into shot-by-shot short-video storyboard scripts. It is intended for text planning and script layout, with separate review before any optional media-generation workflow is used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may move from text-only storyboard drafting into installing or running a third-party media-generation CLI.

Mitigation: Use it as a text-only storyboard assistant unless the user explicitly opts into a separate media-generation workflow after reviewing the CLI and service terms.

Risk: Prompts and selected media files may be sent to dLazy services, and API keys may be stored in local CLI configuration.

Mitigation: Avoid sensitive prompts or media, prefer scoped or environment-provided credentials where appropriate, and rotate or revoke dLazy API keys when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown storyboard script with global video parameters and per-shot fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes aspect ratio, resolution, calculated dimensions, shot descriptions, camera movement, notes, shooting technique, and spoken-script text preserved verbatim from user input.]

## Skill Version(s):

1.2.13 (source: server release evidence; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
