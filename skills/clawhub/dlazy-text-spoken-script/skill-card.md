## Description:

Guides agents in writing conversational, story-driven short-video spoken scripts with a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to draft short-video spoken scripts, character stories, and personal-brand viewpoints from a persona, topic, and audience pain points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The script-writing skill also directs agents to install and run a CLI for image generation and external API calls.

Mitigation: For ordinary spoken-script writing, use a text-only workflow without terminal execution; review the CLI before choosing image generation.

Risk: The dLazy workflow may store an API key locally and transmit prompts or media to dLazy services.

Mitigation: Use this workflow only when those transfers and local key storage are acceptable; avoid submitting sensitive material and protect or rotate API keys as needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown prose with optional shell commands and hosted image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A colloquial, seven-step script is the primary output; the artifact also describes optional dLazy image generation.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
