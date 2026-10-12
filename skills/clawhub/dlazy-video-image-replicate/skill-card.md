## Description:

Studies a reference image or video and helps recreate its look and structure using the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to make images or videos inspired by a supplied reference while substituting their own subjects, products, or characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached media are sent to the dLazy service.

Mitigation: Only attach files you are comfortable sharing with dLazy; avoid sensitive media.

Risk: A dLazy API key is stored locally for authenticated use.

Mitigation: Protect the key and revoke or rotate it if exposed.

Risk: Project sessions can retain prior conversation context.

Mitigation: Use the provided clear-session command when a project should not retain prior context.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text with links to generated image or video results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Follow-up responses can use project conversation context.]

## Skill Version(s):

1.3.28 (source: server-resolved release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
