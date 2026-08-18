## Description:

Converts a blog post or article into a narrated video with storyboard, voiceover, and build support for social or YouTube use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask the dLazy hosted agent to turn blog posts, article text, or article links into narrated videos with project-scoped follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services for processing.

Mitigation: Use the skill only when sending that content to dLazy is acceptable, and avoid attaching sensitive files unless the user's organization permits it.

Risk: The dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Treat the key as a service credential, rotate or revoke it from the dLazy dashboard when needed, and prefer per-invocation environment use on shared systems.

Risk: A global CLI install persists the dLazy binary on the system.

Mitigation: Use the pinned npx invocation when avoiding a persistent global CLI install is preferred.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs an agent to use the pinned dLazy CLI and may reference project IDs, prompts, attached files, authentication setup, and error-handling guidance.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
