## Description:

Hamsa (tryhamsa.com). Use this skill for Hamsa requests that search and read project, voice-agent, and text-to-speech voice data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Hamsa project details, voice agents, available TTS voices, and paginated voice-agent lists through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts that could execute arbitrary code if followed.

Mitigation: Review or replace the oo CLI installation step with an authenticated package manager or a separately downloaded installer with checksum or signature verification.

Risk: The skill relies on user-triggered setup commands when authentication, connection, or billing errors occur.

Mitigation: Run only setup commands you explicitly trust and confirm that they match the observed error before proceeding.

## Reference(s):

- [Hamsa homepage](https://tryhamsa.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hamsa)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
