## Description:

Ship a complete album in one run: write or reuse lyrics, render tracks, generate cover and slideshow art per song, publish either one album film or one video per track plus a playlist, deploy the audio to a radio host, premiere it on air, and fan out the links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickflach](https://clawhub.ai/user/nickflach)

### License/Terms of Use:

MIT-0

## Use Case:

Artists, release operators, and automation-minded teams use this skill to coordinate a full album release across music generation, artwork, video publishing, radio deployment, premiere timing, and announcement fanout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides visible production actions such as uploads, radio deployment, service restarts, premieres, and social announcements.

Mitigation: Run a preflight that lists all targets and public effects, defaults to dry-run, and requires explicit confirmation before any upload, restart, premiere, or announcement.

Risk: Provider credentials, tokens, host configuration, and environment setup can be stale or machine-specific.

Mitigation: Probe token liveness, source the expected environment, compare available adapters with the intended fanout list, and confirm host registration before batch execution.

Risk: Release phases can appear to succeed while silently skipping work, losing uploads, or missing generated assets.

Mitigation: Use ledgers and post-action verification, including non-empty lyric or track ledgers, provider artifact IDs, and video existence checks before playlist creation or fanout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nickflach/skills/album-release)
- [Publisher profile](https://clawhub.ai/user/nickflach)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, markdown]

**Output Format:** [Markdown guidance with configuration shapes, operational steps, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent through release planning and operational execution; it does not bundle the operator-specific runner or credentials.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
