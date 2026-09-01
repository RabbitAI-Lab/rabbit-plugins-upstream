## Description:

Powerful video generation with Kling v3, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos from text prompts or reference images through the dLazy-hosted Kling v3 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may cause prompts, parameters, or local media paths to be sent to a paid external dLazy service.

Mitigation: Invoke the skill only for explicit dLazy or Kling video-generation requests, review prompts and selected files before execution, and use dry-run behavior when cost or payload confirmation is needed.

Risk: API keys may be persisted in the local dLazy configuration file.

Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive environments, restrict access to the local config file, and rotate or revoke keys from the dLazy dashboard when exposure is suspected.

Risk: Reference images or other local media supplied to the CLI are uploaded to dLazy-hosted services for processing.

Mitigation: Avoid submitting confidential media unless the user has approved that cloud processing path and applicable service terms.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns hosted media URLs or asynchronous task identifiers, and can optionally save generated assets to a local path.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
