## Description:

Generates short text-to-video or image-to-video clips with Google Veo 3.1 Fast through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos from text prompts or selected input media through the dLazy hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may invoke dLazy when the user did not clearly choose that service, sending prompts or selected media to dLazy.

Mitigation: Use this skill only for explicit dLazy or Veo requests, and use dry-run when checking costs or payloads.

Risk: Local media paths passed to image or video options may be uploaded to dLazy media storage.

Mitigation: Avoid private files unless the user explicitly intends to upload them, and confirm file paths before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include generated media URLs or async task identifiers returned by the dLazy CLI.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
