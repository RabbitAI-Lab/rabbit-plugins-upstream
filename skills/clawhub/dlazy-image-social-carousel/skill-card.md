## Description:

A structured workflow skill dedicated to social-media carousel design, using a "single-confirmation + cover-first" two-phase flow to plan and generate social carousel images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan social-media carousel narratives, confirm slide direction, generate a cover image first, and then produce remaining slides with consistent visual structure. It supports platforms such as TikTok, Instagram, Xiaohongshu, LinkedIn, and similar carousel workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to run an externally installed npm CLI.

Mitigation: Review the intended @dlazy/cli package version before use and prefer the documented npx invocation when avoiding a persistent global install.

Risk: Prompts and selected media files may be sent to dLazy services.

Mitigation: Use the skill only with media and prompt content appropriate for the dLazy API and storage flow.

Risk: A revocable dLazy API key may be stored locally.

Mitigation: Use dLazy account controls to rotate or revoke the API key when access is no longer needed.

Risk: The reviewed package version is inconsistent across evidence.

Mitigation: Verify which @dlazy/cli version will be installed or executed before using the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with tables, status updates, image-generation command guidance, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the dLazy CLI, send prompts and selected media files to dLazy services, and return generated image URLs hosted by dLazy.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
