## Description:

Helps agents select timezone-aware service capacity windows and record capacity-window ledger entries with overlap reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations planners, support teams, and service agents use this skill to normalize requested service dates and times into explicit capacity windows, then record requested slots in a capacity ledger while identifying overlaps and freeze-window conflicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A host environment could connect the ledger operation to the wrong capacity ledger or permit unintended writes.

Mitigation: Confirm connected tools write only to the intended capacity ledger and require normal user direction before changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/service-capacity-window)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or text responses describing the selected capacity window, ledger entry, and any overlap or freeze-window findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on user-provided capacity requests and host-provided capacity ledger tools when available.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
