## Description:

Text-to-image generation with Jimeng, quickly converting text prompts into high-quality image outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate Jimeng text-to-image outputs through the dLazy CLI and hosted API, with options to save image assets or poll asynchronous jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store a billable dLazy API key in the local user configuration.

Mitigation: Prefer per-invocation credentials or verify restrictive permissions on ~/.dlazy/config.json, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The CLI may upload provided local files to dLazy media storage for model processing.

Mitigation: Confirm file paths and data sensitivity with the user before passing local files to the command.

Risk: Generation requests may consume credits on the user's dLazy organization.

Mitigation: Confirm paid generation actions before execution and use dry-run or balance checks when cost is uncertain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response containing generated image URLs, with optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; generated outputs are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
