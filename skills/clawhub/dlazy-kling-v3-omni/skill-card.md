## Description:

Generates videos from text prompts and optional image or video references using Kling V3 Omni through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate videos from text prompts and optional visual references through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to the third-party dLazy service; generated files are hosted there.

Mitigation: Avoid submitting sensitive prompts or media unless their use with dLazy is approved.

Risk: Login can store a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard when no longer needed.

Risk: Using the skill requires installing or running a third-party npm CLI.

Mitigation: Review the CLI package before use; use npx for non-persistent execution if preferred.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, JSON]

**Output Format:** [CLI JSON response with generated media URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can download a generated asset to a specified local path.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
