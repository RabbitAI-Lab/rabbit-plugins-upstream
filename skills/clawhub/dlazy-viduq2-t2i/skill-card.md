## Description:

Generate high-quality images with Vidu Q2, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images with Vidu Q2 through the dLazy CLI, using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI.

Mitigation: Use the pinned npx invocation for on-demand execution and review the CLI package or source before using it in sensitive environments.

Risk: The dLazy API key is stored in local CLI configuration when saved for repeated use.

Mitigation: Use a revocable dLazy API key, rotate or revoke it when needed, and prefer per-invocation environment variables where persistent local storage is not desired.

Risk: Prompts and selected media files are sent to dLazy's cloud service.

Mitigation: Avoid submitting private media or sensitive prompts unless that transfer is intended and approved for the use case.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [JSON result metadata with image output URLs and optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode may return a task identifier for later polling instead of completed outputs.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter shows 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
