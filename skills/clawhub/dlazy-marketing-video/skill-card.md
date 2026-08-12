## Description:

Create marketing, promotional, advertising, and brand videos from a product, brand, or brief for social media or campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create conversion-focused product and ecommerce marketing videos from product briefs, listings, specs, catalogs, or reference files. It guides use of the dLazy CLI workflow for new or existing video-generation projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product or campaign details, and attached files are sent to dLazy services.

Mitigation: Use the skill only with data approved for dLazy processing and avoid uploading sensitive files unless that transfer is acceptable.

Risk: The skill stores or accepts a dLazy API key, and security evidence notes the pinned CLI does not support the skill's claimed restricted local key-file permissions.

Mitigation: Prefer per-invocation DLAZY_API_KEY in sensitive environments, verify permissions on ~/.dlazy/config.json, and rotate or revoke exposed keys.

Risk: Project sessions can retain context across turns.

Mitigation: Use fresh projects or run --clear for sensitive or unrelated work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload attached local files to dLazy media storage before referencing them in a project.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
