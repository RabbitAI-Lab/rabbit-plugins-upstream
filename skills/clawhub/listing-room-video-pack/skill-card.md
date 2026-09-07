## Description:

Turn listing photos into a labeled set of listing room video clips, one room at a time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate agents and listing teams use this skill to turn inspected listing photos into one labeled short clip per room. It can also guide optional separate narration files or a talking-head intro or outro when the user provides authorized media and scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to Beatra and uploads selected media for remote generation.

Mitigation: Install only if the Beatra service is trusted, inspect media before upload, and submit only the files needed for the requested listing workflow.

Risk: The skill stores and reuses a shared local bearer credential.

Mitigation: Keep the credential only in the private Beatra credential file, avoid exposing tokens in chat or logs, and ask the publisher for narrower per-skill OAuth scopes.

Risk: The workflow can use paid account capabilities for image understanding, video generation, and speech generation.

Mitigation: Show live estimates and paid boundaries before submission, require user confirmation for paid stages, and recover uncertain requests only with the same frozen payload and request identity.

Risk: Silent automatic updates are enabled by default and can replace package files.

Mitigation: Disable automatic checks with the documented update command when review requires pinned files, and review update behavior before installing.

## Reference(s):

- [Listing room video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra skill homepage](https://beatra.ai/skills/listing-room-video-pack)

## Skill Output:

**Output Type(s):** [guidance, shell commands, files, configuration]

**Output Format:** [Markdown guidance with shell commands and generated media file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one labeled video clip per room, with optional separate narration audio files or talking-head intro/outro clips.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
