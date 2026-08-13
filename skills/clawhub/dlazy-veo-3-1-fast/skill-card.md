## Description:

Generates short text-to-video or image-to-video clips with Google Veo 3.1 Fast through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's Veo 3.1 Fast CLI for short video generation from prompts, images, or video-extension inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key may be stored locally in ~/.dlazy/config.json.

Mitigation: Prefer a per-run DLAZY_API_KEY when persistence is not needed, or verify local config permissions after login or auth setup.

Risk: Broad triggers could lead to unintended paid cloud calls.

Mitigation: Review the prompt, media inputs, and cost intent before invocation; use the CLI dry-run mode when a payload or cost estimate is needed first.

Risk: Local files supplied as media inputs may be uploaded to dLazy-hosted storage.

Mitigation: Confirm that each media path is intended for upload and avoid sensitive files unless cloud processing is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link from metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous generation task identifier.]

## Skill Version(s):

1.3.6 (source: server release evidence; artifact frontmatter shows 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
