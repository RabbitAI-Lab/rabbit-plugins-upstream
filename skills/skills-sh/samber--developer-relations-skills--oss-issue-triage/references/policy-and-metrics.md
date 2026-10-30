# Capacity, closing policy and metrics

Contents:

- capacity arithmetic
- the published policy document
- closing and staleness rules
- measurement

## Capacity arithmetic

Derive the response target from capacity; never the reverse.

```
weekly triage capacity (items) = triagers × sessions/week × minutes/session ÷ minutes per item
```

Subtract the hours consumed by items that will never be actionable before comparing against inflow - a queue where most submissions are invalid fails the arithmetic even when nominal capacity looks adequate. Then compare against inflow from the baseline (`triage-baseline.py` prints created vs closed over the window):

- Capacity ≥ inflow → the backlog can shrink; commit to a first-response target and add a backlog burn-down quota per session.
- Capacity < inflow → the queue grows however the labels are arranged. Pull one of step 2's three levers and say which, out loud, in the policy.

A company-backed project usually has paid capacity and possibly contractual response obligations for paying customers - separate those into their own intake path rather than letting them set the target for the volunteer-visible queue. A volunteer project should set a target it can hold during a bad month, not a good one.

## The published policy

Write it in the repository, next to the contributing guide, and link it from the intake forms. Keep it under a page.

```markdown
# How we triage

## What belongs here

Bugs and feature requests. Usage questions → [forum]. Security → [address].

## What to expect

First response: within [N business days]. Not a fix; a human reply.
[Class of items] gets [tighter target] because [reason].

## States

[label]: [what it means, who it waits on, what unblocks it]

## When we close

- Waiting on the reporter for [N] days with no reply.
- Out of scope (with the reason and a link).
- Cannot reproduce after [what was tried].
  Closed is not final: comment with the missing detail and it reopens.

## Who triages

[Rotation, cadence, named backup, how to join.]

## If volume outruns us

[The trigger: inflow rate or valid share, and what we will restrict when it is hit.]
```

Publishing the target converts an unanswered issue from "abandoned project" into "known queue". A policy nobody can meet is worse than none - publish the number the baseline supports.

## Closing and staleness

A defensible configuration of the step-7 rule:

- Restrict the sweep to the waiting-on-reporter state (the `only-labels` mechanism in `actions/stale`; equivalent filters exist elsewhere).
- Exempt the confirmed, accepted, blocked, security and pinned states explicitly.
- Warn first, close later - 14 to 30 days from warning to close is common; `actions/stale` defaults to 60 days idle then 7 days to close.
- Run the first sweep in dry-run mode (`debug-only`) and read the list before it fires. A first live run on an old backlog can close hundreds of items and generate a notification storm that costs the project contributors.
- Make the close message state how to reopen.

Kubernetes' published clocks, each anchored to a named waiting party:

- 20 days without a reporter response → close
- 30 days without assignee action → ask them to produce a patch or release the assignment
- 30 days without owning-group movement → escalate to the group
- 90 days without any activity → mark stale

Backlog bankruptcy (mass-closing everything older than a threshold, with an explanation and an open invitation to reopen) is legitimate exactly once, as the opening move of a new policy. It requires the announcement, the new policy and the new intake to go live the same day. A named practitioner account independently confirms the "exactly once" limit: a maintainer who tried mass-closing everything older than six months found "it works once," then found the backlog back in the same state six months later, because the underlying issue - no natural lifecycle for issues and PRs - was never addressed by the closure itself.

## Metrics

Track four numbers monthly, from the same script that produced the baseline:

- **time to first response** - created → first reply from someone other than the author, bots excluded; whether the published promise is real
- **untriaged share** - open items with no state label ÷ open items; whether triage happens at all
- **queue age** - median and p90 of open items; whether the backlog ages or turns over
- **inflow vs outflow** - created vs closed over the window; whether capacity matches demand

Bot replies and author self-replies are excluded from first response by definition - CHAOSS's _Time to First Response_ and _Issue Response Time_ both make that exclusion explicit, because counting a greeting bot hides the exact delay being measured. Step 9 carries the thresholds and the rule against reading a count metric alone.

Segment first response by whether the opener is a first-time or returning contributor when the export allows it. A project that answers regulars in hours and newcomers in weeks has a contributor-funnel problem invisible in the median.

Don't track:

- total open issue count as a health metric (a growing project grows its queue)
- closed-per-week as a productivity target (it rewards closing hard items without deciding them)

## Review cadence

Re-read the policy against reality:

- quarterly
- immediately after a maintainer joins or leaves
- immediately after a release changes the inflow mix
- immediately after a month where the target was missed more often than met

Adjust the target or the intake, never the definition of what counts as a response.
