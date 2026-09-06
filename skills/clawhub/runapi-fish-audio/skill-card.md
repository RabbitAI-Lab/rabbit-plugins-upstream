## Description:

Guide agents to manage Fish Audio voice resources and generate MP3/WAV speech through RunAPI using the CLI for one-off work or SDKs for production integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover Fish Audio operation contracts, build valid RunAPI requests, execute voice-resource or text-to-speech jobs, and verify returned audio deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Request, response, auth-status, contract, or generated audio files can persist locally after a run.

Mitigation: Use an appropriate workspace, avoid unnecessary sensitive inputs, and remove local files that are no longer needed.

Risk: Created voice resources may persist in the RunAPI/Fish Audio service account.

Mitigation: Create voice resources only when needed, record returned identifiers and state, and manage persistence through the service account outside this skill when required.

Risk: Submitted RunAPI jobs may consume account resources or incur service-side effects.

Mitigation: Submit each request once and retry only when evidence confirms no task was created, no billing occurred, and retrying is safe.

## Reference(s):

- [Fish Audio model overview, pricing, and rate limits](https://runapi.ai/models/fish-audio.md)
- [Fish Audio provider overview](https://runapi.ai/providers/fish-audio.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Fish Audio homepage](https://runapi.ai/models/fish-audio)
- [Fish Audio SDK integration](https://github.com/runapi-ai/fish-audio-sdk)
- [Fish Audio s1 variant](https://runapi.ai/models/fish-audio/s1.md)
- [Fish Audio s2-pro variant](https://runapi.ai/models/fish-audio/s2-pro.md)
- [Fish Audio s2.1-pro variant](https://runapi.ai/models/fish-audio/s2.1-pro.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command blocks, JSON request construction, and validation steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of local request, response, auth-status, contract, and downloaded audio files during execution.]

## Skill Version(s):

0.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
