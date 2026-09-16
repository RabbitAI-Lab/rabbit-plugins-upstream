## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Jimeng Dream Actor workflow, submitting a prompt and one reference image or video to generate an action video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the third-party dLazy npm CLI.

Mitigation: Install only if comfortable running the dLazy CLI; use the documented npx on-demand path when a persistent global binary is not desired.

Risk: The skill stores or uses a dLazy API key for authenticated requests.

Mitigation: Use per-invocation DLAZY_API_KEY when appropriate, and rotate or revoke the key when the service is no longer in use.

Risk: Prompts and selected media files are sent to dLazy cloud endpoints for generation.

Mitigation: Pass only non-sensitive prompts and media files that are appropriate for upload to the dLazy service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload referenced media to dLazy and return hosted result URLs or an async generateId.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
