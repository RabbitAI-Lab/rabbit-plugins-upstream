## Description:

Guides marketing brochure creation from requirements and layout design through user approval and folded or lifestyle mock-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, designers, and other brochure creators use this skill to plan and generate branded brochure layouts, confirm the design, and produce folded and lifestyle mock-ups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy cloud endpoints for generation.

Mitigation: Use only content approved for third-party cloud processing and review referenced media before submitting it.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect local credentials; use the per-session environment variable where appropriate and rotate or revoke exposed keys.

Risk: Running the third-party CLI requires trusting its npm package.

Mitigation: Review the package and source before installation; the documented npx invocation is an alternative to a persistent global install.

## Reference(s):

- [dLazy CLI source (tool referenced in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Image links]

**Output Format:** [Conversational text and Markdown with image URLs and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an approved brochure layout before folded and lifestyle mock-ups; generated images are hosted by dLazy.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
