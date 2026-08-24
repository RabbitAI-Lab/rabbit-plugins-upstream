## Description:

Turns a script, screenplay, or shot list into a storyboarded, shot-by-shot video workflow using dLazy's hosted storyboard agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn scripts, scene breakdowns, and shot lists into multi-shot storyboard and video-generation projects through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files are sent to dLazy's hosted service.

Mitigation: Use the skill only when third-party SaaS processing is intended, and avoid sending sensitive files or prompts unless that transfer is approved.

Risk: The CLI can save an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials or rotate and revoke saved keys through the dLazy dashboard when needed.

Risk: Broad trigger terms can invoke a third-party video-generation workflow earlier than expected.

Mitigation: For ambiguous script, storyboard, or video requests, confirm the user wants to use dLazy before running the CLI.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from dLazy and may reference project-scoped sessions, uploaded files, and generated video workflow outputs.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
