## Description:

A structured workflow skill for planning and generating social-media carousel images with a single-confirmation, cover-first process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and design-oriented agents use this skill to plan social-media carousel narratives, confirm the cover direction, and generate matching image slides through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy cloud services for prompts and uploaded media.

Mitigation: Install only if cloud processing is acceptable for the intended content, and avoid sending sensitive media unless approved.

Risk: A saved dLazy API key can continue to authorize requests after setup.

Mitigation: Use npx for temporary CLI use where appropriate, and rotate or revoke the API key from the dLazy dashboard when access is no longer needed.

Risk: Global installation of the dLazy CLI leaves a long-lived tool on the system.

Mitigation: Prefer the pinned npx invocation when a persistent global CLI is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with planning tables, status updates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and uses user confirmation before generation; prompts and media may be sent to dLazy cloud endpoints.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
