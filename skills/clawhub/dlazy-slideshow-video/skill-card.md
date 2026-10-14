## Description:

Helps turn slides or documents into narrated slideshow videos with voiceover and transitions using the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users can ask an agent to turn presentations or documents into narrated explainers, training videos, or report summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files can be sent to the third-party dLazy service.

Mitigation: Only submit prompts and files that you are comfortable sharing with dLazy.

Risk: The CLI may store an API key locally and a global install persists on the system.

Mitigation: Protect and rotate the key as needed; use the pinned npx invocation if a persistent global install is undesirable.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with inline shell commands and service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy service produces the slideshow video; attached files are uploaded to that service.]

## Skill Version(s):

1.0.26 (source: ClawHub release metadata; skill frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
