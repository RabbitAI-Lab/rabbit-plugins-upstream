## Description:

Turns a document, topic, or brief into a narrated explainer, courseware, or training video with outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create narrated explainer, report broadcast, courseware, or training videos from documents, topics, and briefs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local files may be sent to dLazy services for hosted processing.

Mitigation: Avoid attaching confidential documents unless organizational policy permits that service.

Risk: API keys can be stored in the local dLazy CLI config.

Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive environments, and revoke or rotate stored keys when needed.

Risk: The skill depends on the external dLazy CLI package and remote API availability.

Mitigation: Use the pinned @dlazy/cli version from the artifact metadata and review CLI source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked dLazy service may produce video artifacts, streamed status, project ids, or error messages.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter is 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
