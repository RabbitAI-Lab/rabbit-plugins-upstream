## Description:

Studies a user-provided reference image or video, then recreates the same look and structure with the user's own subject, product, or characters through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to recreate the visual style and structure of reference images or videos while substituting their own subject, product, or characters. The skill supports starting a new dLazy template project or continuing an existing project through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages, options, and attached local files may be sent to dLazy hosted services.

Mitigation: Avoid attaching sensitive files unless needed, and use the skill only when comfortable with dLazy's hosted service.

Risk: Authentication depends on a dLazy API key stored in local configuration or supplied through the environment.

Mitigation: Protect the local config, avoid exposing DLAZY_API_KEY, and rotate or revoke the key if exposure is suspected.

Risk: Continuing an existing project can reuse prior session context.

Mitigation: Confirm the project ID before continuing prior work, and clear or compact sessions when appropriate.

Risk: The skill invokes a third-party CLI package.

Mitigation: Prefer npx or another isolated execution method over a global install, and review the CLI source or package provenance before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project IDs, uploaded file URLs, authentication state, and streamed CLI responses.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter shows 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
