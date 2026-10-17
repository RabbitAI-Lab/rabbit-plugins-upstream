## Description:

Manage sales leads locally. Use when adding prospects, scoring leads, setting follow-ups, tracking conversions, or viewing funnels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xueyetianya](https://clawhub.ai/user/xueyetianya)

### License/Terms of Use:

MIT-0

## Use Case:

Sales employees and business operators use this skill to manage a local lead pipeline, including adding prospects, scoring leads, scheduling follow-ups, converting leads, and viewing funnel reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lead records may include personal, customer, and deal information stored in plaintext under ~/.leads/leads.json.

Mitigation: Use restrictive filesystem permissions for ~/.leads and leads.json, avoid shared machines for sensitive CRM data, and review local data retention practices before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xueyetianya/skills/leads)
- [BytesAgain Homepage](https://bytesagain.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text command output and local JSON data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores lead records locally in ~/.leads/leads.json.]

## Skill Version(s):

3.4.1 (source: server release metadata; artifact frontmatter says 3.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
