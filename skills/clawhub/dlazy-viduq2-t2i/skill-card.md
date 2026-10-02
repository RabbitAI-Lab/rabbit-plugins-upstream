## Description:

Guides an agent to generate or edit images with Vidu Q2 through the dLazy cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate or edit images from prompts and optional reference images using Vidu Q2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images may be sent to dLazy cloud endpoints.

Mitigation: Avoid sensitive prompts and private files unless uploading them to dLazy is acceptable.

Risk: Authentication can store a dLazy API key in the user's local configuration.

Mitigation: Keep the user configuration private and rotate or revoke the key if exposed.

Risk: A global CLI install persists beyond the task.

Mitigation: Use the documented pinned npx invocation when a persistent global installation is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executed commands can return image URLs or asynchronous task IDs.]

## Skill Version(s):

1.3.24 (source: ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
