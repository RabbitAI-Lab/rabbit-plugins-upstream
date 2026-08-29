## Description:

Turns slides, photos, or documents into narrated slideshow-style videos with voiceover and transitions through the dLazy file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn presentations, documents, photos, or slide-like source material into explainer, report, courseware, or training videos. It helps an agent start or continue a dLazy project using the pinned file-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local files are sent to dLazy hosted services for video generation.

Mitigation: Confirm before uploading confidential documents and use the skill only when dLazy hosted processing is acceptable.

Risk: A global CLI installation persists an executable on the user's system.

Mitigation: Use the pinned npx invocation when a persistent global CLI install is not desired.

Risk: The skill requires a dLazy API key for authenticated use.

Mitigation: Use the documented login or auth flow, keep the key scoped to the user's organization, and rotate or revoke it from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses project-scoped dLazy CLI conversations; attached local files may be uploaded to dLazy storage through the CLI.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
