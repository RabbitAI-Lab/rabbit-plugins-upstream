## Description:

Guides agents through marketing brochure design from requirements gathering and layout planning to confirmed mock-up generation using a layout-first approval workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, marketers, and agent operators use this skill to plan brochure structure, generate layout-first brochure artwork, confirm the layout, and then create folded and lifestyle mock-ups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local reference media may be sent to dLazy cloud endpoints for brochure generation.

Mitigation: Avoid uploading sensitive media unless cloud processing is intended, and review generated outputs before reuse.

Risk: The dLazy CLI may store an API key in a local configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable when local key persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global installation of a third-party CLI changes the local tool environment.

Mitigation: Review the @dlazy/cli package or source before installation, or use the pinned npx invocation for one-off runs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with image-generation prompt drafts, confirmation checkpoints, shell commands, and generated asset URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, uses the dLazy CLI, and requires explicit user confirmation before moving from layout generation to mock-up production.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
