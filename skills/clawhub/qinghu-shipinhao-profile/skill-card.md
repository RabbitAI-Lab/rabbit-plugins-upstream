## Description:

Retrieves WeChat Channels account profile details and statistics for account research and operations analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and analysts use this skill to look up a WeChat Channels account's homepage profile and statistics for account research and operational analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrade of Node and qhkit can change the user's environment beyond the profile lookup task.

Mitigation: Use a preinstalled, trusted Node and qhkit environment; require explicit review before installation or upgrades.

Risk: Unpinned package installation and saved credentials can expose the environment or Qinghu API token.

Mitigation: Use a reviewed package version and avoid persisting credentials without the user's informed consent.

Risk: Profile lookups consume paid Qinghu credits.

Mitigation: Estimate credits and obtain the user's consent before making paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-profile)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summary; file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile and statistics lookup requires a Qinghu API token and paid credits.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
