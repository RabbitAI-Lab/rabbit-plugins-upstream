## Description:

Generates short text-to-video or image-to-video clips with Google Veo 3.1 Fast through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request short Google Veo 3.1 Fast video generations or extensions through dLazy's hosted video-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted API and file service.

Mitigation: Confirm the user intends to use dLazy's hosted service and pass only explicit, user-approved prompts and media paths.

Risk: A dLazy API key may be stored locally or supplied through DLAZY_API_KEY.

Mitigation: Store keys only in the documented user config or environment, restrict local access, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party npm CLI package.

Mitigation: Use the pinned @dlazy/cli version from the skill metadata and review the package or source before installing in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown instructions with bash commands and JSON CLI output examples; generated media may be returned as hosted URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy API and file endpoints.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
