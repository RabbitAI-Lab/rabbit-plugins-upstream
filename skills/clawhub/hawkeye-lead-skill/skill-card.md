## Description:

招商线索池 is an operations skill for Hawkeye merchant_lead workflows, exposing ten CLI commands for private and public lead lists, lead statistics, lead details, claiming and assigning leads, and updating follow-up status, remarks, and acceptance priority.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yiqingqiu23187](https://clawhub.ai/user/yiqingqiu23187)

### License/Terms of Use:

MIT-0

## Use Case:

Operations staff and authorized agents use this skill to inspect Hawkeye private and public merchant leads, review lead details and statistics, and perform controlled lead-management updates through a local Node.js CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The detail lookup can return plaintext phone numbers when --plain-phone is used.

Mitigation: Use --plain-phone only for an explicit business need after user approval, and otherwise rely on the default masked-phone behavior.

Risk: One detail lookup mode can silently advance a private lead's follow-up status.

Mitigation: Warn the user before detail lookups that request plaintext phones and confirm that the status side effect is acceptable.

Risk: Mutating commands can change real lead records in a production-like test lane.

Mitigation: Preview the request with --dry-run, show the exact request body to the user, and run mutating commands only with explicit approval and --confirm.

Risk: Stored browser-derived access tokens can expose authorized Hawkeye lead access if retained unnecessarily.

Mitigation: Install only for authorized operators, verify the target domain before use, and remove the stored token when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yiqingqiu23187/skills/hawkeye-lead-skill)
- [Publisher profile](https://clawhub.ai/user/yiqingqiu23187)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with CLI commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI provides --help and --schema introspection, --dry-run previews, and --confirm gating for mutating commands.]

## Skill Version(s):

0.1.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
