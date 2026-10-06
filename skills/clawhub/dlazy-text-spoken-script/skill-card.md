## Description:

Guides agents in writing story-driven short-video spoken scripts using a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to draft conversational short-video scripts with a strong hook, a concrete story, and a memorable closing line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises spoken-script writing but also directs the agent to run an unrelated image-generation workflow.

Mitigation: Review the full skill before installation and do not run image-generation steps unless they match the user's request.

Risk: Using the dLazy CLI can send prompts to a remote service and requires local API-key authentication.

Mitigation: Obtain approval before installing or authenticating the CLI, and avoid sending sensitive prompts or media without authorization.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Paragraph-form spoken script; the separate image workflow may provide commands and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven-part story structure; colloquial language intended for spoken delivery]

## Skill Version(s):

1.3.26 (ClawHub release; supplied skill file says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
