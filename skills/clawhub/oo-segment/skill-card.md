## Description:

Segment (segment.com). Use this skill for ANY Segment request, including Segment-related searching, reading, and event submission through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Segment through an OOMOL-connected account, inspect live action schemas, and send Segment Alias, Batch, Group, Identify, Page, Screen, or Track calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that the skill is presented as read/search-oriented while its available actions submit or mutate Segment analytics data.

Mitigation: Use it only when the user intends to send Segment events, traits, page or screen views, group links, aliases, or batches; confirm the exact action, payload, and destination account before running.

Risk: The security guidance flags the fallback pipe-to-shell installer path as requiring independent trust and verification.

Mitigation: Avoid the remote installer path unless the OOMOL CLI installer has been independently trusted and verified; prefer an already installed and authenticated CLI.

## Reference(s):

- [ClawHub Segment Skill](https://clawhub.ai/oomol/skills/oo-segment)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Segment Homepage](https://segment.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action-schema inspection before constructing Segment connector payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
