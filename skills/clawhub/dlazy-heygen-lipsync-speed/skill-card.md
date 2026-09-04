## Description:

Runs dLazy's HeyGen Lipsync Speed model to create fast lip-sync output from supplied video and audio inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content automation agents use this skill to invoke a hosted dLazy/HeyGen lip-sync workflow for videos that need rapid audio-to-mouth synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio inputs are sent to dLazy/HeyGen services for processing.

Mitigation: Use only media that is approved for external cloud processing and avoid sensitive or restricted inputs unless the organization has approved that workflow.

Risk: Authentication can store a dLazy organization API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication when persistent local storage is not desired, and rotate or revoke organization keys when access changes.

Risk: The artifact contains documentation mistakes in the usage example and output sample.

Mitigation: Check `dlazy heygen-lipsync-speed -h` or use `--dry-run` before relying on example commands in automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON results with hosted output URLs; optional local file download when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when --no-wait is used.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
