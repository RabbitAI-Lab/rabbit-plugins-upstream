## Description:

Helps agents generate videos with Tongyi Wanxiang 2.7 from text, first and last frames, or reference media through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate short videos from prompts, reference images or videos, or specified first and last frames through a hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy cloud services.

Mitigation: Avoid submitting sensitive prompts or files without approval; review the service terms before uploading.

Risk: The external CLI requires an API key and can save it locally.

Mitigation: Protect the local CLI configuration, or provide the key per invocation; rotate or revoke compromised keys.

Risk: Installing a third-party npm CLI introduces dependency trust considerations.

Mitigation: Review the linked CLI source and package before installing the pinned version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source and documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report hosted media URLs or asynchronous task IDs returned by the CLI.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
