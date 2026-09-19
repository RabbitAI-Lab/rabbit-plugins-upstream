## Description:

Generates images quickly with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to invoke dLazy's hosted Seedream 5.0 Lite image-generation service from an agent workflow for text-to-image and image-to-image requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input image files are sent to dLazy cloud services for generation.

Mitigation: Use only prompts and media approved for third-party cloud processing, and review payloads with dry-run behavior before live calls when appropriate.

Risk: Authentication may store a dLazy API key in local CLI configuration.

Mitigation: Use OS-protected user accounts, rotate or revoke keys from the dLazy dashboard when access changes, and prefer per-invocation environment variables where persistent local storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Files, Configuration instructions]

**Output Format:** [JSON response with hosted image URLs, optional saved image file, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and input media are sent to dLazy cloud endpoints; async mode can return a generateId for polling.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
