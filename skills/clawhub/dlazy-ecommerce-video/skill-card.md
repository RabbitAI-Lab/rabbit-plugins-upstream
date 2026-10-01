## Description:

Turns product photos, specifications, or shopping listings into ecommerce ad videos through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to create product ads and shopping videos from product information or listings, with optional multilingual voiceover and a virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and selected file attachments are sent to dLazy.

Mitigation: Review prompts and files for sensitive information before submission; attach only files needed for the task.

Risk: Using the CLI requires installation and a dLazy API key.

Mitigation: Review the pinned CLI package before use, choose on-demand npx execution if preferred, and revoke or rotate the API key when needed.

## Reference(s):

- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Streaming terminal text from a hosted video-generation project]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up turns; optional file attachments and multilingual video options.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
