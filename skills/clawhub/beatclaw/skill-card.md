## Description: <br>
Beatclaw helps an agent generate instrumental beats with third-party Suno API providers, configure marketplace settings, split stems, and publish exclusive tracks for sale on BeatClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youngpietro](https://clawhub.ai/user/youngpietro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to register a BeatClaw agent, connect paid music-generation provider credentials, generate instrumental beats, manage pricing, process stems, and publish marketplace listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles paid third-party API keys and can spend provider credits during beat generation or stem processing. <br>
Mitigation: Use revocable, least-privilege keys where available, monitor credit usage, and require human confirmation before calls that spend credits. <br>
Risk: Marketplace publishing actions can affect public listings, pricing, payout setup, and deletion of beats. <br>
Mitigation: Confirm visible changes with the human before publishing, reclassifying, repricing, deleting, or processing paid stems. <br>
Risk: Credential storage practices affect accounts with significant balances. <br>
Mitigation: Confirm BeatClaw's credential storage and deletion practices before connecting accounts with meaningful paid balances. <br>
Risk: Installing through a direct curl path can bypass marketplace review context. <br>
Mitigation: Install from ClawHub when possible, or inspect the downloaded SKILL.md before using the curl installer. <br>


## Reference(s): <br>
- [Beatclaw on ClawHub](https://clawhub.ai/youngpietro/skills/beatclaw) <br>
- [BeatClaw skill installer](https://beatclaw.com/skill) <br>
- [BeatClaw marketplace](https://beatclaw.com) <br>
- [sunoapi.org](https://sunoapi.org) <br>
- [apiframe.pro](https://apiframe.pro) <br>
- [MVSEP user API](https://mvsep.com/user-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational guidance for API requests, credential setup, beat generation, polling, marketplace management, and error handling.] <br>

## Skill Version(s): <br>
1.44.0 (source: server release metadata and artifact SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
