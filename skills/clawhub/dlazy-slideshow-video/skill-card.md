## Description:

Turns slides and documents into narrated slideshow videos with voiceover and transitions through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users can turn presentations or documents into narrated explainers, training videos, and report summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached files are uploaded to dLazy's hosted service.

Mitigation: Attach only documents and images you intend to share with dLazy.

Risk: The CLI requires an API key and may store it locally.

Mitigation: Treat the key as a credential; rotate or revoke it through the dLazy dashboard if needed.

Risk: Installing a third-party CLI may expose sensitive documents to its behavior.

Mitigation: Review the CLI and its source before use with sensitive files; use the pinned npx option instead of a global install when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and CLI instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy service produces narrated slideshow videos; the CLI streams project responses.]

## Skill Version(s):

1.0.23 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
