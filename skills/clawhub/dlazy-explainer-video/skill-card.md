## Description:

Turns a document, topic, or brief into a narrated explainer video workflow covering outline, storyboard, voiceover, build, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to request narrated explainer, courseware, report broadcast, or training videos from documents, topics, or briefs through the dLazy CLI service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy, and uploaded files may be stored by its media service.

Mitigation: Use the skill only for content approved for dLazy's hosted service, and review service terms before sending sensitive or regulated documents.

Risk: The dLazy CLI may save an API key in the local user configuration.

Mitigation: Protect the local config file, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The skill depends on a third-party npm CLI and hosted API endpoints.

Mitigation: Review the pinned CLI package or source before installation and use the pinned npx invocation when avoiding a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and streamed CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project identifiers, uploaded files, or generated explainer-video artifacts returned by the hosted service.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
