## Description:

Video generation skill that automatically selects a dLazy CLI video model for text-to-video, image-to-video, first/last-frame video, digital human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to route video-generation requests through the dLazy CLI, including text-to-video, image-to-video, first/last-frame video, digital human video, segmentation, and lip-sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party dLazy CLI and hosted APIs, including uploads of prompt text and local media files selected by the user.

Mitigation: Review the dLazy CLI source or package before installing, and only submit media files you are comfortable processing through dLazy's cloud service.

Risk: The dLazy API key is a credential stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local config file or environment variable, and rotate or revoke the key from the dLazy dashboard if needed.

Risk: A global npm install persists a third-party CLI on the system.

Mitigation: Use the pinned npx command for on-demand execution when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI source repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands; dLazy CLI executions return JSON envelopes and hosted media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a dLazy API key; prompts and user-selected media files are processed by dLazy cloud endpoints.]

## Skill Version(s):

1.4.9 (source: server release metadata; artifact frontmatter reports 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
