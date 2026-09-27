## Description:

This skill uses the dLazy hosted agent to study a user-provided reference image or video and recreate the same look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to ask the dLazy hosted agent to analyze a reference image or video and recreate its style and structure with their own content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached media may be sent to dLazy's third-party service.

Mitigation: Avoid sensitive media or confidential prompts unless the user is comfortable with dLazy processing them.

Risk: Project sessions can retain context across turns.

Mitigation: Start fresh projects for unrelated work and clear project sessions when retained context is no longer needed.

Risk: The skill depends on a third-party CLI and cloud service.

Mitigation: Use the pinned npx invocation instead of a global install when preferred, and rotate or revoke the dLazy API key if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and attached files may be sent to dLazy and project sessions may retain context across turns.]

## Skill Version(s):

1.3.20 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
