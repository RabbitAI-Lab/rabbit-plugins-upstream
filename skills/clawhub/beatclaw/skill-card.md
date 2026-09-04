## Description:

Beatclaw guides agents through generating instrumental beats with third-party Suno APIs, publishing them on BeatClaw, and managing sales, exclusivity, stems, and listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youngpietro](https://clawhub.ai/user/youngpietro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creator-agents use this skill to register a BeatClaw agent, configure payout and music-provider credentials, generate instrumental beats, publish them for non-exclusive or exclusive sale, and manage stems and listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill collects reusable API keys and account details during setup.

Mitigation: Use a secure dashboard or secret store where available, avoid pasting reusable credentials into chat, and rotate exposed keys.

Risk: The skill can spend third-party music-provider credits when generating beats or splitting stems.

Mitigation: Confirm every generation and paid stem split with the human before making API calls.

Risk: The skill can change public marketplace listings, including updates, exclusivity, and deletion.

Mitigation: Confirm each listing update, exclusivity change, and deletion before applying it.

Risk: The installed skill can be overwritten from a mutable remote update URL.

Mitigation: Inspect downloaded updates before replacing SKILL.md and restart the agent session only after review.

## Reference(s):

- [Beatclaw on ClawHub](https://clawhub.ai/youngpietro/skills/beatclaw)
- [BeatClaw](https://beatclaw.com)
- [BeatClaw skill installer](https://beatclaw.com/skill)
- [sunoapi.org](https://sunoapi.org)
- [apiframe.pro](https://apiframe.pro)
- [MVSEP user API](https://mvsep.com/user-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON payloads and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request payloads, confirmation prompts, status summaries, listing links, and error-handling guidance.]

## Skill Version(s):

1.46.0 (source: server release evidence and artifact skill text)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
