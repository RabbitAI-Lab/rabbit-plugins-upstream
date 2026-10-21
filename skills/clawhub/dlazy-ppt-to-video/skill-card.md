## Description:

Helps turn presentations into narrated explainer, pitch, courseware, or training videos using the dLazy file-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating training, educational, or presentation videos use this skill to guide a dLazy project from source slides through an outline, storyboard, narration, and video production. The underlying service also accepts other documents, so users should confirm the intended scope before attaching files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached presentations or other documents may be uploaded to a third-party service, including confidential content.

Mitigation: Use only files approved for sharing with dLazy; review their contents before attaching them.

Risk: The PPT-focused description expands to broader document-to-video tasks.

Mitigation: Prefer explicit presentation-to-video requests and confirm scope before uploading other documents.

Risk: Using the service requires a dLazy API key that may be stored locally.

Mitigation: Keep the key private and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with instructions and project responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up conversations; video production is handled by the dLazy service.]

## Skill Version(s):

1.0.29 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
