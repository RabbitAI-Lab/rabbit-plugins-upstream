## Description:

Doubao Speech (volcengine.com) helps agents operate Doubao Speech through OOMOL-connected CLI actions for speech-to-text and text-to-speech tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Doubao Speech action schemas, submit asynchronous speech-to-text or text-to-speech jobs, and retrieve task status and outputs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer commands that pipe downloaded scripts directly into Bash or PowerShell.

Mitigation: Install the oo CLI through a verified, versioned, organization-approved method, or inspect and pin the installer before execution.

Risk: Write actions can submit asynchronous speech-to-text or text-to-speech jobs that may consume account credits or create remote tasks.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running submit_stt or submit_tts.

## Reference(s):

- [Doubao Speech homepage](https://www.volcengine.com/product/doubao-voice)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live connector schemas, JSON payloads, execution IDs, task status, and Doubao Speech task outputs.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
