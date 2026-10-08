## Description:

Helps turn presentations and documents into narrated explainer, training, or pitch videos through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing presentations, lessons, pitches, or reports use this skill to guide the creation of narrated videos from slides and other documents with dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI.

Mitigation: Review the CLI before installation; use the version-pinned npx command if a global install is not desired.

Risk: Authentication requires a dLazy API key stored locally or supplied for each invocation.

Mitigation: Protect the key and rotate or revoke it if exposed.

Risk: Attached documents are uploaded to dLazy's hosted service.

Mitigation: Attach only files you intend to share with that service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text and command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation is handled by the dLazy hosted service.]

## Skill Version(s):

1.0.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
