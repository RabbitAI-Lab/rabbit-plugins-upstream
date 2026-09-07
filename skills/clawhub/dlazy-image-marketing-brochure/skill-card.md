## Description:

A workflow skill for designing marketing brochures, guiding requirements alignment, layout generation, confirmation, folded mock-ups, and lifestyle mock-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketing teams, and designers use this skill to plan and generate marketing brochure layouts, folded mock-ups, and lifestyle mock-ups through a dLazy cloud image-generation workflow with user confirmation gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the npm-based dLazy CLI can execute third-party code on the user's machine.

Mitigation: Review the @dlazy/cli package or source, pin the intended CLI version, and prefer npx or an isolated environment over a global install when possible.

Risk: The workflow stores and uses a dLazy API key for cloud generation.

Mitigation: Use a scoped dLazy API key and rotate or revoke it if it is exposed or no longer needed.

Risk: Local media paths provided to the CLI may be uploaded to dLazy services.

Mitigation: Only provide media files intended for upload and avoid sensitive or unrelated assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, prompt drafts, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication; selected media paths may be uploaded to dLazy services when provided.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
