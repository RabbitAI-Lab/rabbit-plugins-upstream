## Description:

High-fidelity text-to-vector generation for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative production teams use this skill to have an agent generate vector-oriented assets through the dLazy Recraft V4 Pro Vector CLI. It supports prompt-driven illustration and production asset workflows with optional local saving of generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external npm CLI and stores or reads a dLazy API key for authenticated requests.

Mitigation: Review the CLI source or package provenance before installation, prefer npx or a contained environment over global install, and rotate or revoke the API key if exposure is suspected.

Risk: Prompts, parameters, and any supplied local media paths are sent to dLazy-hosted API and file services.

Mitigation: Pass only files and prompt content intended for upload, and avoid sending sensitive data unless the deployment has approved the dLazy service for that use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Results are returned as hosted file URLs or downloaded to a local path with --save; asynchronous runs return a generateId for polling.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
