## Description:

Guides agents through creating ecommerce spokesperson videos with portrait recipes and a script-to-voice-to-avatar-to-B-roll workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and ecommerce teams use this skill to plan and produce product-selling avatar videos, including portrait selection, scripts, voiceovers, lip-synced footage, B-roll, and assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the paid dLazy CLI/API can incur charges.

Mitigation: Review expected cost and use --dry-run where available before generating media.

Risk: Local product images and media may be uploaded to dLazy services.

Mitigation: Upload only media you are comfortable sharing with dLazy.

Risk: A dLazy API key may be saved in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable if you prefer not to save the key in ~/.dlazy/config.json.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [Portrait recipes](artifact/recipes.md)
- [Production pipeline](artifact/pipeline.md)
- [Troubleshooting and compliance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown instructions with example commands and prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation requires a separate paid dLazy service; assembling the final video requires an additional editing step.]

## Skill Version(s):

1.0.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
