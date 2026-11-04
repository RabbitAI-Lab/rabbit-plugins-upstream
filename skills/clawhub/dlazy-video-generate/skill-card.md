## Description:

Generates videos from text or reference media by selecting a suitable dLazy CLI video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate short videos from prompts, images, video, or audio, including image animation and lip-sync workflows. It selects a dLazy video model and returns generated video outputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy cloud services, and local media files are uploaded for processing.

Mitigation: Use only media you intend and are authorized to upload; avoid sensitive material unless your organization permits it.

Risk: The API key grants access to the user's dLazy organization.

Mitigation: Prefer the device login flow over sharing a key in chat, keep credentials private, and rotate or revoke keys when needed.

Risk: The external CLI package and cloud service were not fully audited.

Mitigation: Review the CLI and service terms before using them with sensitive workloads; the documented CLI install pins package version 1.2.3.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)

## Skill Output:

**Output Type(s):** [Video files, Shell commands, Guidance]

**Output Format:** [Generated video URLs and CLI JSON envelopes, with command guidance in text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference media may be uploaded to dLazy cloud storage; generated outputs are returned as hosted URLs.]

## Skill Version(s):

1.4.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
