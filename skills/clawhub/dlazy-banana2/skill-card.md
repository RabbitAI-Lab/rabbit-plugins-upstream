## Description:

Generate and edit high-quality images with Nano Banana 2.0, including text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to invoke the dLazy Banana 2 image-generation CLI for text-to-image and image-to-image work. It helps agents authenticate, construct commands, pass optional image inputs, and understand returned image URLs or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media files passed to the CLI can be uploaded to dLazy's hosted service.

Mitigation: Review prompts and files before use, and do not submit sensitive material unless dLazy's service terms and organizational policy allow it.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Prefer OS user-restricted storage or per-invocation environment variables, and rotate or revoke keys when access is no longer needed.

Risk: The skill depends on a third-party hosted service and third-party CLI package.

Mitigation: Install only if you are comfortable using dLazy's service, keep the package pinned, and review the linked source or npm package before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI may return hosted image URLs, asynchronous task IDs, or downloaded image files when --save is used.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter shows 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
