## Description:

Helps turn documents into explainer, report, or training videos through a project-based dLazy assistant for outlining, storyboarding, narration, and production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to guide a hosted assistant through converting documents into explainers, report recaps, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy's hosted service and file storage.

Mitigation: Only submit content approved for processing by dLazy; review documents before attaching them.

Risk: The CLI can save an API key locally, and a global installation persists on the device.

Mitigation: Protect and rotate the API key as needed; use the pinned npx option if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (linked in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped responses; video generation is handled by the hosted service.]

## Skill Version(s):

1.0.24 (source: ClawHub release metadata; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
