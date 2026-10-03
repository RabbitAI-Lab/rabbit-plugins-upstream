## Description:

Turns a website URL into a promotional video, social ad, or product demo using a hosted dLazy workflow for site capture, branding, storyboarding, voiceover, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn website links into promotional videos, social ads, and product demos through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the external dLazy service.

Mitigation: Review content and attachments before submission; avoid sharing sensitive material without approval.

Risk: Login stores an API key locally unless an environment variable is used.

Mitigation: Protect the local credential or use the per-invocation environment-variable option.

Risk: Installing the third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the pinned npm package and its source before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses project-scoped conversations; video production runs through the hosted dLazy service.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
