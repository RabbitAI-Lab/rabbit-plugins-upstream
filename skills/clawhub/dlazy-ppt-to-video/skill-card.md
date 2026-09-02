## Description:

Helps agents turn PPT, PowerPoint, Keynote, and other documents into explainer, courseware, pitch, or training videos using dLazy's file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to start or continue dLazy file-to-video projects for presentation and document-to-video generation. Typical tasks include explainer videos, pitch videos, courseware, report summaries, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and attached documents may be sent to dLazy's hosted API and file storage.

Mitigation: Use the skill only for documents intended for that service, avoid sensitive files unless approved, and review applicable service terms and organizational policy.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-run DLAZY_API_KEY or npx when persistence is undesirable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The PPT-focused release branding may be narrower than the broader document-to-video workflow used by the skill.

Mitigation: Confirm that the requested task is presentation or document-to-video generation before invoking the dLazy file-to-video workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI commands, project continuation guidance, file attachment handling, authentication setup, and error-handling guidance.]

## Skill Version(s):

1.0.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
