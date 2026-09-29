## Description:

Helps turn documents into explainer, report, and training videos through dLazy's hosted video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating explainer, report, or training videos from documents can use this skill to start and continue a dLazy video project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached documents and prompts are sent to dLazy's hosted service.

Mitigation: Share only documents and prompts approved for upload to dLazy.

Risk: The dLazy CLI requires an API key that may be saved locally.

Mitigation: Use a per-invocation key or on-demand npx when lower persistence is needed, and rotate or revoke saved keys when no longer needed.

Risk: Using this skill installs or runs the third-party dLazy CLI.

Mitigation: Review the CLI before installing or running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming terminal text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through a project-scoped hosted service.]

## Skill Version(s):

1.0.19 (source: ClawHub release evidence; skill frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
