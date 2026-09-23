## Description:

Generate or edit high-quality images with Nano Banana 2.0 using text-to-image or image-to-image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images through the dLazy hosted Nano Banana 2.0 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to the third-party dLazy cloud service.

Mitigation: Confirm the user is comfortable sharing the prompt and any referenced files with dLazy before uploading sensitive content.

Risk: Generated files are hosted by dLazy and returned as hosted URLs.

Mitigation: Review generated outputs and storage expectations before sharing or relying on the returned URLs.

Risk: The dLazy CLI may store an API key in the user's local configuration.

Mitigation: Use OS account protections, rotate or revoke the key from the dLazy dashboard when needed, and use the DLAZY_API_KEY environment variable for per-invocation credentials when preferred.

Risk: Image generation can fail because of insufficient credits, missing credentials, invalid local file paths, service errors, or safety policy enforcement.

Mitigation: Use dry-run or status checks where appropriate, handle documented CLI error codes, and guide the user to authenticate or recharge only when the returned error indicates that action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)
- [dLazy API Key Dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned as dLazy-hosted file URLs; optional save commands can download assets locally.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
