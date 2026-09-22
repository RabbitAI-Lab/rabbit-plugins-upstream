## Description:

MiniMax Hailuo omni-modal video generation skill for creating 5-15 second clips with native stereo audio, text-to-video prompting, frame transitions, and multi-asset references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's MiniMax H3 video-generation workflow from an agent, supplying prompts, first/last frames, or reference media and receiving generated media URLs or task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to the skill are sent to dLazy services for cloud generation.

Mitigation: Avoid sending sensitive prompts or media unless the user is comfortable uploading them to dLazy.

Risk: The workflow depends on an external npm CLI and may store credentials in the user's local dLazy configuration.

Mitigation: Review the dLazy CLI/source before installation, and use npx or DLAZY_API_KEY when the user prefers not to keep a global binary or stored API key.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or async task identifiers; local media supplied as parameters is uploaded through the dLazy CLI.]

## Skill Version(s):

1.2.16 (source: server release metadata; artifact frontmatter is 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
