## Description:

Compare workspace access lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and collaboration administrators use this skill to compare current workspace membership against an approved list and identify additions, removals, role changes, and external entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace membership lists can contain sensitive organizational access information.

Mitigation: Only provide ACL JSON that is appropriate for the current agent session and avoid including credentials or unrelated private data.

Risk: An incorrect approved_members list can produce a misleading access delta.

Mitigation: Confirm that both current_members and approved_members reflect the intended workspace before acting on the comparison.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/workspace-access-checklist-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Concise access delta, commonly represented as a JSON-compatible object with optional Markdown explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The access_delta object contains workspace_id, added, removed, role_changed, and external_entries.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
