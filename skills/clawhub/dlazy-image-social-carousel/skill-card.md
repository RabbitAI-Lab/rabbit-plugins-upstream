## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to plan social-media carousel content, confirm its direction and cover, and guide consistent slide generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy's cloud service for generation.

Mitigation: Review prompts and selected images before each run, and send only material you are comfortable sharing with dLazy.

Risk: The skill requires a dLazy API key, and generation may involve account costs.

Mitigation: Protect or revoke credentials as needed, use the documented credential option that suits your environment, and confirm costs before generation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown planning tables and structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-confirmed, phased carousel planning; generated images are handled separately through dLazy services.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
