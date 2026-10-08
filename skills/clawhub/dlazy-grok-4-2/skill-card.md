## Description:

Generates text, answers questions, and supports reasoning with Grok 4.2 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke this skill for text generation, conversational answers, and reasoning tasks using the dLazy-hosted Grok 4.2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat triggers may send prompts to dLazy unexpectedly.

Mitigation: Invoke the skill explicitly and avoid sending sensitive prompts or private files unless you intend to share them with dLazy.

Risk: Using the third-party CLI requires trusting an external package.

Mitigation: Review the @dlazy/cli package before installing it globally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI repository (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may be delivered asynchronously.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
