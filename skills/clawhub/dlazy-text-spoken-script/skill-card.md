## Description:

Generate high-contrast, resonant, and story-driven spoken scripts for short videos, character stories, and personal IP scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, social media teams, and agents use this skill to draft short video spoken scripts from a persona, topic, or audience pain point. The script is structured around a hook, suspense, story, viewpoint, experience, persona connection, and punchline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release presents itself as a spoken-script writer while artifact behavior also encourages installation and use of a networked image-generation CLI.

Mitigation: Review the skill before installation and only enable CLI execution when image generation through dLazy is intentionally in scope.

Risk: The referenced CLI may store API credentials locally and make outbound requests to dLazy services.

Mitigation: Use least-privilege API keys, rotate or revoke keys when no longer needed, and verify that outbound network access to api.dlazy.com and files.dlazy.com is acceptable.

Risk: Artifact behavior indicates local media paths can be uploaded for cloud processing.

Mitigation: Do not provide sensitive local media unless upload to the dLazy hosted service is approved for the use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown prose with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces spoken-script paragraphs following a seven-step creative structure; artifact guidance also references optional dLazy CLI use.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
