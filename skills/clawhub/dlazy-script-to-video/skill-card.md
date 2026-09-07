## Description:

Turns a script, screenplay, or shot list into a storyboarded, shot-by-shot video workflow that breaks down scenes, generates shots, assembles, and validates video output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn scripts or scene breakdowns into storyboarded, multi-shot videos through dLazy's hosted storyboard agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only for content that is appropriate to upload to dLazy, and avoid attaching sensitive files unless the user accepts that service boundary.

Risk: The skill depends on an npm-distributed CLI and can be installed globally.

Mitigation: Prefer the pinned npx invocation or a local install, and review the CLI package before installing globally.

Risk: The dLazy API key is stored in local CLI configuration or provided through an environment variable.

Mitigation: Protect the API key like any service credential and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy-hosted project state and generated media artifacts when the hosted service creates them.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
