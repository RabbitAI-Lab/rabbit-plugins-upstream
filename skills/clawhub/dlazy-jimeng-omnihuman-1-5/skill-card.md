## Description:

Generates realistic digital-human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request dLazy-hosted Jimeng OmniHuman 1.5 generation from a portrait image plus audio or text and receive hosted result URLs or saved media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI can store a dLazy organization API key in local configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY when tighter control is needed, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Prompts and selected portrait or audio media are sent to dLazy-hosted endpoints for generation.

Mitigation: Avoid passing private or sensitive media unless cloud upload to dLazy is intended and approved for the use case.

Risk: The security summary flags inconsistent safety and output documentation.

Mitigation: Review the generated result and task status before relying on the output, especially for user-facing or brand-sensitive video generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON response with hosted media URLs, optional downloaded media files, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; local image or audio inputs are uploaded to dLazy endpoints; async mode returns a task ID for polling.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
