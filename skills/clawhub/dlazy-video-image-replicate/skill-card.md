## Description:

Studies a user-provided reference image or video, then helps recreate the same look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to invoke the dLazy hosted video-image-replicate agent for reference-based image or video recreation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests, prompts, and attached local files are sent to dLazy hosted services during normal use.

Mitigation: Review attached files before upload and use a fresh or cleared project for sensitive work.

Risk: The skill requires a dLazy API key that is stored locally or passed through the environment.

Mitigation: Keep the API key scoped and revocable, rotate or revoke it when needed, and prefer one-off npx use if a persistent global CLI is not desired.

Risk: Project sessions can preserve context across turns.

Mitigation: Clear the project session before sensitive or unrelated work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and plain-text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted project sessions and uploaded user files through the dLazy CLI.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
