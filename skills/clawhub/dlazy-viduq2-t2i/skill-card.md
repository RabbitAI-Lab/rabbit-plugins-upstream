## Description:

Generate high-quality images with Vidu Q2, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy-hosted Vidu Q2 CLI using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy-hosted services.

Mitigation: Confirm that prompt content and uploaded files are appropriate for a hosted image-generation provider before running the command.

Risk: Authentication stores or uses a dLazy API key.

Mitigation: Use the documented login or auth flow, keep local config access restricted, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The skill depends on a third-party npm CLI package and can be installed globally.

Mitigation: Prefer the pinned npx invocation where practical and review the referenced CLI source or npm package before installation.

Risk: Image generation may make billable hosted API calls.

Mitigation: Use dry-run or confirm expected costs before generation, especially when processing private or high-volume inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are returned as hosted file URLs and may be downloaded locally with the CLI save option.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter is 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
