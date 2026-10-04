## Description:

Helps turn a creative idea into a reviewed video-production plan, canvas workflow, and generated media through dLazy services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan a story-to-video workflow, review its stages, and build a canvas pipeline for characters, scenes, shots, and a final video. It also describes optional dLazy CLI-assisted media generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Executing an external CLI from the terminal may run unreviewed package code or leave a persistent global install.

Mitigation: Review the CLI package before use and prefer a contained environment or on-demand npx invocation over global installation.

Risk: Prompts and referenced media are sent to dLazy services for processing.

Mitigation: Confirm that content is appropriate to share with the service before generation.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect local credentials, use a per-session environment variable when appropriate, and rotate or revoke exposed keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source (referenced by skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown plan summaries and instructions; canvas workflow shapes after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return links to generated media when the external CLI is used.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; bundled frontmatter says 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
