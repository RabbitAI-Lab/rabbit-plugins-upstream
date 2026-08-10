## Description:

Riffkit helps agents turn a TikTok link, uploaded video, analyzed template, or written creative direction into short AI-generated riff or ad videos with optional character, product placement, language, captions, hashtags, and a strategy recap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and product teams use this skill through an agent to plan, confirm, submit, monitor, and retrieve short-form riff videos and UGC-style ad creatives from Riffkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heartbeat can overwrite the local skill definition from riffkit.ai without checksum or signature verification.

Mitigation: Disable automatic overwrite or add checksum/signature validation plus a backup and rollback path before enabling heartbeat auto-updates.

Risk: The skill contacts riffkit.ai with a Riffkit session cookie and can upload selected videos or images.

Mitigation: Use the device authorization flow, confirm the purpose of each file before upload, and limit uploads to intended media.

Risk: Video generation and retries can make paid Riffkit calls after user confirmation.

Mitigation: Require explicit pre-submit confirmation, do not retry silently, and state the cost before retrying failed or cancelled tasks.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit skill source](https://riffkit.ai/SKILL.md)
- [Riffkit heartbeat source](https://riffkit.ai/HEARTBEAT.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown instructions with API endpoint references, shell command examples, status summaries, download links, captions, hashtags, and strategy recap]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authenticated riffkit.ai API access; paid generation is gated by explicit user confirmation.]

## Skill Version(s):

1.3.1 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
