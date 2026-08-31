## Description:

A workflow skill for planning and generating marketing brochure layouts, folded mock-ups, and lifestyle mock-ups through dLazy CLI image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to plan brochure content, generate layout artwork first, confirm it, then create folded and lifestyle mock-ups for marketing materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a third-party dLazy account and API key.

Mitigation: Confirm account and key handling before installation, and rotate or revoke the key from the dLazy dashboard when access is no longer needed.

Risk: Brochure prompts and uploaded reference files may be sent to dLazy cloud services.

Mitigation: Avoid submitting confidential, regulated, or customer-sensitive content unless the intended dLazy service use is approved.

Risk: A global CLI install leaves the dLazy CLI available on the system after the task.

Mitigation: Use the documented npx invocation when a temporary execution path is preferred.

Risk: Generated brochure layouts and mock-ups may contain inaccurate copy, branding, or regulated-industry claims.

Mitigation: Use the skill's layout confirmation gate and review final assets for brand, legal, and compliance accuracy before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and image-generation prompt drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication and user confirmation before each generation step.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter is 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
