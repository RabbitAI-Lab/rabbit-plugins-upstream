## Description:

Turns a script or scene breakdown into a storyboarded, shot-by-shot video workflow with scene breakdown, shot generation, assembly, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to invoke dLazy's storyboard template for multi-shot videos from scripts, scene breakdowns, and optional reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and attached files may be sent to dLazy services.

Mitigation: Use the skill only with content intended for dLazy processing, and avoid attaching confidential media or scripts unless upload is intended.

Risk: A global CLI install persists a local executable and user configuration.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy service may produce video project artifacts outside the skill card workflow.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
