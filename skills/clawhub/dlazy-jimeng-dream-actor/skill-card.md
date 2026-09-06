## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Jimeng Dream Actor image-to-video generation from a prompt and a selected character image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected media files are sent to dLazy cloud endpoints for processing.

Mitigation: Use the skill only with media and prompts that are appropriate to share with dLazy, and review service terms before use.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use npx or DLAZY_API_KEY for one-off use when persistence is not desired, and check permissions on ~/.dlazy/config.json after login.

Risk: Generation requests can consume dLazy credits.

Mitigation: Use dry-run or review cost behavior before running large jobs, and monitor account credits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous generation task identifier.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter declares 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
