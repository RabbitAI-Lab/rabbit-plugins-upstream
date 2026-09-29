## Description:

Separates image foregrounds from backgrounds and returns a transparent-background image URL for product photos, portraits, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to remove backgrounds from product or portrait images and retrieve transparent image results for editing or composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chosen local images are uploaded to dLazy's hosted service.

Mitigation: Only submit images you are authorized to share and review the service terms before use.

Risk: Authentication stores a dLazy API key in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Using the skill requires installing and running an external npm CLI.

Mitigation: Review the pinned CLI source and package before installation when supply-chain assurance is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown guidance; CLI result is JSON containing a hosted image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result can be saved locally; asynchronous requests return a task ID before the image is ready.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
