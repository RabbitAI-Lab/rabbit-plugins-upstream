## Description:

Turns product photos, documents, or shopping listings into ecommerce ad videos with optional multilingual narration and a virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketers use this skill to turn product information or storefront listings into short promotional videos for online shops and social commerce.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product or reference files are sent to dLazy's hosted service.

Mitigation: Attach only files and enter only information you are comfortable sending to dLazy.

Risk: Signing in stores a dLazy API key locally for later CLI use.

Mitigation: Review the local credential storage before signing in, and rotate or revoke the key if needed.

Risk: A global CLI installation persists on the local machine.

Mitigation: Use the documented npx option if you do not want a persistent global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video]

**Output Format:** [Streaming text response and generated video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Videos can include multilingual voiceover and an optional virtual host.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata; source file frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
