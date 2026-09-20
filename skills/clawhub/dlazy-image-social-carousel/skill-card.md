## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, marketers, and agents use this skill to plan and generate social-media carousel image sets with a single direction confirmation, cover-first review, and matched remaining slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a third-party CLI and cloud service that may receive prompts and referenced media files.

Mitigation: Confirm the dLazy service is acceptable for the intended data before use, and avoid sending sensitive media or prompts unless approved.

Risk: A persistent global CLI install and local API key configuration can leave credentials on the user's machine.

Mitigation: Use npx for non-persistent execution when appropriate, and rotate or revoke the dLazy API key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with confirmation tables, concise planning text, inline shell commands, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication; prompts and referenced media may be sent to dLazy cloud endpoints.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
