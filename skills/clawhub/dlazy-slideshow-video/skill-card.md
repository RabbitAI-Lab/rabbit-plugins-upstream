## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users can turn slides or documents into narrated explainer, training, or report videos through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the hosted dLazy service.

Mitigation: Only submit prompts and files you intend to share with dLazy.

Risk: Authentication saves a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: Using the skill requires installing or running a third-party CLI.

Mitigation: Review the pinned CLI package before use; use npx if a global installation is unwanted.

## Reference(s):

- [dLazy CLI source (skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped conversations can continue across turns; video generation is handled by the hosted service.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
