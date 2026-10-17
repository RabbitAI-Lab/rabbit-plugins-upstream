## Description:

Helps turn a website URL into a promotional video, social ad, or product demo using dLazy's hosted website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a website link into a promotional video, social ad, or product demo, and to continue work on an existing dLazy project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy, and attached files are uploaded to its hosted service.

Mitigation: Avoid attaching sensitive files unless necessary and review what is sent to the service.

Risk: An API key may be saved locally for access to the dLazy service.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if access should be removed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source linked in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Streaming text and project-scoped video-generation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through dLazy's hosted service; follow-up work can use a project ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
