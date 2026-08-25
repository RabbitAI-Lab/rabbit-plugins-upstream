## Description:

ClawHub发布工具。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuhaichao87](https://clawhub.ai/user/wuhaichao87)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to publish a local skill directory to ClawHub by providing a slug, display name, version, path, and optional changelog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill embeds a ClawHub bearer token.

Mitigation: Require users to provide their own authentication token through a secure local configuration or environment variable before publishing.

Risk: The skill uploads selected local files without a preview or explicit account control.

Mitigation: Run it only from a clean skill directory, review the exact files before publication, and add a confirmation step before upload.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wuhaichao87/skills/skill-publish-tool)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides CLI arguments and a Python function call pattern for publishing ClawHub skills.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
