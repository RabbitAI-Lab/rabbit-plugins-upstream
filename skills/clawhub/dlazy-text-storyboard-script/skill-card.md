## Description:

Generates detailed short-video storyboard scripts from user-provided themes, outlines, or structured copy while preserving spoken script text verbatim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and video teams use this skill to convert themes, outlines, or structured copy into shot-by-shot short-video storyboard scripts. The output includes video parameters, scene direction, camera movement, shooting notes, technique, and spoken script sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents a text-only storyboard workflow while also including dLazy CLI installation, terminal execution, third-party API calls, possible media uploads, and persistent local API key storage.

Mitigation: Review before installation and use only when those dLazy CLI behaviors are expected; remove or split the media-generation and terminal-execution sections for a text-only storyboard release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown storyboard script with video parameters and per-shot sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves user-provided spoken script text verbatim and defaults video ratio and resolution when omitted.]

## Skill Version(s):

1.2.5 (source: server release evidence; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
