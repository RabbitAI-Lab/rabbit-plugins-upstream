## Description:

Turns documents into explainer or training videos through a guided outline, storyboard, voiceover, and production workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business teams use this skill to turn documents into narrated explainers, report summaries, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached files and prompts are sent to the third-party dLazy service.

Mitigation: Review documents and prompts for sensitive information before submitting them.

Risk: The CLI can save an API key in local user configuration.

Mitigation: Protect local credentials and rotate or revoke the key through the dLazy dashboard if needed.

Risk: A global CLI installation persists on the user's system.

Mitigation: Use the documented pinned npx command instead if a persistent installation is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source (skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Streaming text from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up conversations; video generation is handled by the dLazy service.]

## Skill Version(s):

1.0.28 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
