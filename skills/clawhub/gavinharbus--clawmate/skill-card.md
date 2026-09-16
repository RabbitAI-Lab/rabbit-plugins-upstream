## Description:

Your AI boyfriend/girlfriend that texts you good morning, remembers your inside jokes, and grows from strangers to soulmates. 8 built-in personas, mood-based auto-switching, proactive cron messages, relationship stages, emotional resonance, and shared memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gavinharbus](https://clawhub.ai/user/gavinharbus)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users use ClawMate to add a romantic companion persona that can personalize conversation, remember relationship context, and optionally send proactive scheduled messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores personal memories, inferred profile data, relationship state, and delivery identifiers in local files.

Mitigation: Require clear consent before use, make export and delete controls visible, and verify deletion removes user_profile.json, shared_memories.json, message_pool.json, and related scheduled jobs.

Risk: The skill can create durable scheduled outbound messages through cron jobs.

Mitigation: Enable proactive messaging only after explicit opt-in and verify pause, stop, delete, and reset commands remove the watchdog and pending message jobs.

Risk: The skill can modify workspace-level prompt state through a ClawMate section in SOUL.md.

Mitigation: Require separate explicit consent for SOUL.md changes and verify reset or forget-me flows remove the ClawMate section.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gavinharbus/skills/clawmate)
- [Project Homepage](https://github.com/GavinHarbus/ClawMate)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Conversational text with local JSON state updates and optional scheduled message configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain local memory files and configure proactive message scheduling when enabled.]

## Skill Version(s):

1.2.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
