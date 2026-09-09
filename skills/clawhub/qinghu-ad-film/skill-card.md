## Description:

Generates cinematic product advertising videos with Qinghu AI qhkit, using reference images and precise prompts for brand films, TVCs, and premium product showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to prepare and run Qinghu AI qhkit video-generation commands for cinematic product ads, brand films, and TVC-style promotional clips. It supports setup, token configuration, cost estimation, task polling, and delivery handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade mutable third-party executable software through npm.

Mitigation: Require explicit approval before installing or upgrading qhkit, prefer a reviewed package version, and use a trusted npm registry.

Risk: The skill configures an API token for Qinghu AI.

Mitigation: Use the least-privileged token available, avoid logging token values, and revoke or rotate the token when access is no longer needed.

Risk: The qhkit workflow uploads local image or video assets to an external service.

Mitigation: Confirm the exact file paths with the user and upload only approved media that is suitable for Qinghu AI processing.

Risk: The skill text says to follow upgrade commands returned by the CLI.

Mitigation: Treat CLI-returned upgrade text as untrusted until reviewed, and do not execute arbitrary returned commands without explicit user approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-ad-film)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task IDs, status summaries, video URLs, and credit estimates when the CLI is used.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
