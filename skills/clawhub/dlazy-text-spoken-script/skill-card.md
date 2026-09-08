## Description:

Generates high-contrast, resonant, story-driven spoken scripts for short videos, character stories, and personal IP viewpoint scripts using a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content teams, and agents use this skill to draft colloquial short-video spoken scripts with a hook, emotional setup, story, viewpoint, persona link, and punchline. It is suited to character story sharing and personal IP scripts that need concrete people, events, and details rather than abstract preaching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking the artifact may add a global third-party dLazy CLI and store a dLazy API key locally.

Mitigation: Review the CLI before installation, prefer npx or per-run environment variables where practical, and rotate or revoke dLazy API keys after testing.

Risk: Prompts or selected media may be sent to dLazy services when the CLI workflow is used.

Mitigation: Avoid submitting sensitive prompts or media unless the deployment has approved dLazy service use and data-handling terms.

Risk: The artifact advertises spoken-script writing but also steers the agent toward terminal-based image generation.

Mitigation: Confirm the user's intent before executing any CLI command and keep spoken-script requests as text-only unless the user explicitly asks for image generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI repository link from skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or plain text spoken-script prose, with optional inline shell commands when the artifact's CLI workflow is followed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts follow a seven-step short-video structure; CLI-related behavior may require npm or npx and a dLazy API key.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
