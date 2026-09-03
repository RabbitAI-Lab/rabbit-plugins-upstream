## Description:

Tongyi Wanxiang 2.7 video model covers text-to-video, first/last-frame-to-video, and reference-to-video generation through the dLazy hosted CLI service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short videos from prompts, reference media, or first and last frames using dLazy's Wan 2.7 CLI wrapper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and user-provided media are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only with content that is acceptable to upload to dLazy's service, and review payloads with the CLI dry-run option when appropriate.

Risk: API keys may be stored in the local dLazy CLI configuration.

Mitigation: Use the per-run DLAZY_API_KEY option when persistent credentials are not desired, restrict permissions on ~/.dlazy/config.json, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global CLI installation adds a persistent npm package to the user's environment.

Mitigation: Use the pinned npx invocation or review the pinned package and source before installing globally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, saved local files, or asynchronous task identifiers depending on CLI flags.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
