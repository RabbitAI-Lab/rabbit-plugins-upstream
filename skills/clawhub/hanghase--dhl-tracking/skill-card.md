## Description:

DHL Tracking is a read-only parcel tracking skill that polls DHL shipment status, stores local shipment state, and reports status changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanghase](https://clawhub.ai/user/hanghase)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to track one or more DHL parcels from an agent workflow, refresh shipment status on demand, and view localized status changes without logging in to DHL or changing delivery options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shipment tracking numbers, postal codes, and DHL-returned recipient or status details are stored locally and sent to DHL during add or refresh operations.

Mitigation: Install only when this local storage and DHL request behavior is acceptable; avoid adding shipments whose tracking details should not be stored in the agent workspace.

Risk: DHL's public tracking endpoint is not guaranteed to accept the same request format indefinitely.

Mitigation: Use the included doctor command and review refresh errors when DHL endpoint behavior changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hanghase/skills/dhl-tracking)
- [DHL public tracking endpoint](https://www.dhl.de/int-verfolgen/data/shipment)
- [Publisher profile](https://clawhub.ai/user/hanghase)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration]

**Output Format:** [Console text and local JSON state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores setup and shipment state locally as UTF-8 JSON; refresh output reports only shipment status changes.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
