## Description:

Builds recurring social content calendars by drafting fresh carousels, single-image posts, and short videos, then scheduling them through PostNitro to LinkedIn, Instagram, TikTok, and Threads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iammuneeb](https://clawhub.ai/user/iammuneeb)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers, founders, and marketing teams use this skill to configure recurring social posting routines, generate fresh platform-specific creative, schedule approved posts through PostNitro, and audit recent publishing failures before adding new calendar slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved scheduling can affect live brand social channels.

Mitigation: Keep initial runs in draft, and review selected accounts, recurring cadence, post status, and scheduled/public approval before allowing live scheduling.

Risk: Incorrect account, cadence, timezone, or calendar history choices can place posts in the wrong slots or miss prior publishing failures.

Mitigation: Confirm the filled configuration with the user, query the selected accounts and scheduled-post history, and report failed or partially failed posts before adding new content.

Risk: Retrying imports after timeouts can create duplicate designs or posts.

Mitigation: Use the async import-then-poll workflow, poll the existing job after timeouts, and retry scheduling with the created design ID instead of re-importing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iammuneeb/skills/recurring-content-calendar)
- [PostNitro capability facts](https://postnitro.ai/facts)
- [PostNitro LLM reference](https://postnitro.ai/llms-full.txt)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown guidance with structured social post copy, platform settings, and scheduling summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-approved PostNitro connection, social account IDs, cadence, timezone, and publish status before live scheduling.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
