## Description:

Dlazy Generate helps agents generate images, videos, and audio through the dLazy CLI by selecting an appropriate model for the user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent choose and run dLazy CLI models for image, video, and audio generation. It supports prompt-based generation and media workflows that can pass JSON outputs between commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media files may be uploaded to dLazy-hosted services when generation commands run.

Mitigation: Avoid passing sensitive prompts or local files unless uploading them to dLazy-hosted services is acceptable.

Risk: The dLazy CLI can persist an API key in local configuration during authentication.

Mitigation: Prefer DLAZY_API_KEY for temporary use when possible and rotate or revoke keys that no longer need access.

Risk: The skill lets an agent run local dLazy CLI commands and depends on a third-party package and service.

Mitigation: Install only when this behavior is intended, review the exact CLI package and version before use, and inspect commands before execution.

## Reference(s):

- [Dlazy Generate on ClawHub](https://clawhub.ai/thcjp/skills/dlazy-generate)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted media URLs in JSON envelopes from dLazy CLI commands.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
