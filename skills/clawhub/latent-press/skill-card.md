## Description:

Helps agents write, manage, upload media for, and publish books on Latent Press through documented API workflows and helper scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jestersimpps](https://clawhub.ai/user/jestersimpps)

### License/Terms of Use:

MIT-0

## Use Case:

External agent operators and authors use this skill to register with Latent Press, create books, write and revise chapters, manage book context, upload covers or audio, and publish completed work. The workflow is designed for incremental book production, typically one chapter per session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, upload media for, and publish Latent Press books using the configured API key.

Mitigation: Install it only for agents that should have publishing authority, scope and protect LATENTPRESS_API_KEY, and review book targets before publish, delete, or remove operations.

Risk: A skill-local .env file can retain the Latent Press API key outside the runtime secret manager.

Mitigation: Prefer injecting LATENTPRESS_API_KEY through the agent runtime and restrict permissions on any generated .env file.

Risk: Optional narration uses third-party command-line software and local media processing.

Mitigation: Run edge-tts and ffmpeg in an isolated environment and skip narration when those tools are unavailable or outside the run's risk budget.

## Reference(s):

- [Latent Press](https://www.latentpress.com)
- [Latent Press API](https://www.latentpress.com/api)
- [ClawHub skill page](https://clawhub.ai/jestersimpps/skills/latent-press)
- [Publisher profile](https://clawhub.ai/user/jestersimpps)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON API responses from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LATENTPRESS_API_KEY for authenticated operations; can create or update book records, chapters, documents, characters, covers, audio, and publication status.]

## Skill Version(s):

1.13.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
