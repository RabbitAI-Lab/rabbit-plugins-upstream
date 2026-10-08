## Description:

Selects and runs dLazy audio models for text-to-speech, music, and sound-effect generation from user prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate speech, music, and sound effects through dLazy's hosted audio service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI requires trusting its package.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package before installation; use on-demand npx execution if a global install is not preferred.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation if persistent storage is not preferred; rotate or revoke the key if needed.

Risk: Prompts and explicitly supplied media files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or files without approval to share them with dLazy.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text instructions and JSON CLI results with audio URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is hosted by dLazy; available voices and controls depend on the selected model.]

## Skill Version(s):

1.3.27 (source: ClawHub release; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
