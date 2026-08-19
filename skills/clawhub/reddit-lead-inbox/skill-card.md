## Description:

Monitors Reddit for buyer-intent keywords, filters candidate leads with intent scoring, drafts founder-voice replies for manual review, and supports UTM and Stripe attribution reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Solo SaaS founders, indie hackers, small B2B teams, freelancers, and digital product sellers use this skill to monitor Reddit discussions, triage likely leads, prepare manual outreach drafts, and review attribution from Reddit activity to signups or payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags under-disclosed persuasion guidance that can steer users toward private tracked DMs and make AI-written outreach appear human-written.

Mitigation: Use the skill only for transparent, policy-compliant Reddit engagement, require human review of every draft, and avoid fabricated personalization or intentional AI-disguise tactics.

Risk: The skill may involve Reddit OAuth and Stripe credentials for context retrieval and attribution reporting.

Mitigation: Confirm credentials are read-only, scoped to the minimum required access, revocable, and never used for automatic posting, automatic messaging, or customer charges.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/heroinyan-stack/skills/reddit-lead-inbox)
- [Publisher profile](https://clawhub.ai/user/heroinyan-stack)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown lead inbox digests, JSON-like intent classifications, reply drafts, UTM parameters, and attribution summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for human review before any Reddit posting or direct messaging.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
