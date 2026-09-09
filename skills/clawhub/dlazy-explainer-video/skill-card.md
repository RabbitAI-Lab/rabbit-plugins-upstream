## Description:

Turns a document, topic, or brief into a narrated explainer video by guiding outline, storyboard, voiceover, generation, and validation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn documents, topics, reports, courseware, or briefs into narrated explainer and training videos through dLazy project sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected files may be sent to dLazy as a hosted service.

Mitigation: Use the skill only with content approved for dLazy processing and avoid attaching sensitive files unless that use is authorized.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use least-privileged environments for first use and rotate or revoke the dLazy key when access is no longer needed.

Risk: The skill depends on npm or npx execution of the pinned dLazy CLI package.

Mitigation: Prefer npx for first use, avoid elevated installs, and review the pinned package/source before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-selected files and return generated video artifacts or links through dLazy project sessions.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
