## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Jimeng Dream Actor workflow from an agent, providing prompts and image or video references to generate action-video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths supplied to the skill are sent to dLazy services for processing.

Mitigation: Avoid submitting sensitive media or prompts unless dLazy's terms and data handling are acceptable for the use case.

Risk: The skill requires a dLazy API key and may consume account credits during generation.

Mitigation: Use a revocable API key, rotate it when needed, and use dry-run or account controls before running costly generations.

Risk: The skill depends on the third-party dLazy CLI package.

Mitigation: Prefer npx or an isolated environment over a persistent global install, and review the CLI source or package before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated media URLs or an asynchronous generateId; the --save option can download the generated asset locally.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
