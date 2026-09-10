## Description:

Turns a script, screenplay, or shot list into a storyboarded, shot-by-shot video workflow using the dLazy hosted storyboard agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and production teams use this skill to invoke the dLazy storyboard template for multi-shot animated video generation from scripts, scene breakdowns, character references, and prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, options, and attached files to the dLazy hosted API and media storage.

Mitigation: Only attach files intended for upload to dLazy and avoid sending sensitive content unless the user has approved that use.

Risk: The dLazy API key is an account credential that may be saved in the local CLI configuration.

Mitigation: Protect the local config file, prefer per-invocation environment variables when appropriate, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: A global CLI install persists a local executable on the system.

Mitigation: Use the pinned npx invocation or review the dLazy CLI source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package and requires a dLazy API key for hosted SaaS execution.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
