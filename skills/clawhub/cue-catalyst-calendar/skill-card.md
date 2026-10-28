## Description:

Builds a date-ordered calendar of disclosed or statute-derived catalysts for a user's holdings, without speculative events, date arithmetic, or trading judgments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research teams use it to organize verified upcoming disclosure and statutory events for their holdings into a traceable watch calendar.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection instructions may expose the API key outside the intended service.

Mitigation: Use the user-supplied announcement path without configuring an API key until both connection methods enforce approved HTTPS destinations and reject unsafe redirects.

Risk: Sending issuer interests to Cue may reveal sensitive investment interests.

Mitigation: Review whether sharing holdings or issuer interests with Cue is acceptable before connecting.

Risk: A calendar date may still be incorrect even when the checker reports PASS.

Mitigation: Manually verify calendar dates against their cited sources.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-catalyst-calendar)
- [Event taxonomy](artifact/references/event-taxonomy.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance, Shell commands]

**Output Format:** [Markdown calendar with a JSON Lines source ledger, evidence snapshots, and progress notes]

**Output Parameters:** [Holdings and a date window]

**Other Properties Related to Output:** [Chronologically ordered events use disclosed dates or statute-derived dates with traceable sources; the skill does not provide forecasts or trading judgments.]

## Skill Version(s):

0.1.28 (source: server release, changelog, released 2026-10-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
