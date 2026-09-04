## Description:

Turns a user's idea into an end-to-end video production pipeline covering story, characters, 3-view portraits, scenes, shots, keyframes, shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and production teams use this skill to turn a creative brief into a structured idea-to-video workflow, including a user-reviewed plan, canvas expansion, model-backed media generation steps, and final video assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and referenced media to dLazy cloud services for generation.

Mitigation: Use it only with content suitable for dLazy services and review the service/data handling expectations before sending prompts or media.

Risk: The skill requires npm/npx or a global dLazy CLI installation and asks the agent to run terminal generation commands.

Mitigation: Prefer npx or review the global install first, then approve one generation command at a time.

Risk: Using dlazy login or dlazy auth set can store a dLazy API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for environment-scoped credentials when persistent local config is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured plan summaries and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-gated workflow plans and command guidance for dLazy CLI/API execution; generated media URLs are returned by the external service.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter says 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
