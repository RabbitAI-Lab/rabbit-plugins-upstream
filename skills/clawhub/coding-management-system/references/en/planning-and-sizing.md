# Planning And Sizing

Size the goal after it reaches `Ready for Planning`. Size reflects uncertainty, risk, acceptance breadth, and coordination, not AI typing speed.

## Size Matrix

| Dimension | Small | Medium | Large |
| --- | --- | --- | --- |
| Delivery surface | One narrow behavior or component | Related multi-file or one-subsystem change | Cross-subsystem, migration, architecture, or release |
| Acceptance | Directly testable | Several criteria or one important user flow | Multiple flows, environments, or stakeholder decisions |
| Uncertainty | Known approach | Some discovery or integration uncertainty | Material unknowns or competing designs |
| Risk | Local and reversible | Moderate regression or data risk | Production, security, data integrity, deployment, or broad regression risk |
| Coordination | One agent can implement and verify | Developer plus independent evaluation | Planner, Developer, QA, and possibly Owner |

Choose the highest size indicated by any material dimension.

## Ten-Stage Authorization

| Size | Stage ceiling | Review horizon | Default governance |
| --- | ---: | ---: | --- |
| Small | 30 minutes | 5 hours | Lite |
| Medium | 60 minutes | 10 hours | Standard |
| Large | 120 minutes | 20 hours | Full |

Authorize up to ten stages. Time is a ceiling, not a quota or delivery promise. Finish early when evidence proves success.

A stage is a timeboxed outcome checkpoint. A coding loop is an implement-verify-evaluate cycle inside a stage. A stage is not a Milestone, Work Order, handoff, or document.

Suggested stage purposes:

1. Orient and confirm the authorized outcome.
2. Establish baseline or reproduce the problem.
3. Deliver the first vertical slice; run alignment check.
4. Complete core behavior.
5. Integrate related components.
6. Exercise the primary user flow; run alignment check.
7. Cover material edge cases and failure handling.
8. Run regression, quality, and maintainability checks.
9. Rehearse acceptance in the real target environment.
10. Consolidate evidence and run terminal alignment/QA review.

Adapt or skip stage purposes when the work finishes sooner. Do not fill time with extra features.

## State-Based Resizing

| State change | Action |
| --- | --- |
| Stable `In Progress` with useful evidence | Keep size |
| First local `Needs Fix` with known cause | Keep size; bounded repair |
| Two consecutive core or QA failures | Escalate one size or re-plan |
| Scope estimate grows over 20 percent | Re-size before continuing |
| User flow fails while automatic checks pass | Keep work open and strengthen functional evidence |
| `Locally Compliant, Globally Misaligned` | Stop execution and run direction alignment |
| `Owner Decision Required` or `Blocked` | Stop the autonomous clock |
| `Ready for Review` | Spend remaining effort on evidence, not expansion |

Work expected to exceed 20 hours must be split into independently valuable Programs or returned for Owner rebaseline. Do not authorize an unreviewed 30-40 hour run.

## Planning Output

Produce:

- one-sentence user-visible outcome;
- minimum useful scope;
- Non-Goals;
- acceptance criteria and failure examples;
- size and reasons;
- governance profile;
- stage ceiling and alignment points;
- risks and Owner decisions;
- one first stage outcome;
- evidence required before acceptance.
