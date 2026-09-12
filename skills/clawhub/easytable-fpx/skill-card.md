## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI, including listing booking areas, dates, and times, looking up bookings by phone, and cancelling bookings through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they need one-shot shell guidance for checking easyTable availability or managing bookings without running the easytable MCP server. It is suited to authorized booking workflows where the user can pair fpx with their own browser session and review any real booking change before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to grant persistent, domain-scoped browser proxy access to easyTable.

Mitigation: Install only if this browser-proxy access is acceptable, scope it to easyTable, and revoke the extension or pairing when finished.

Risk: The skill documents actions that can cancel, create, or modify real restaurant bookings.

Mitigation: Use only for bookings the user is authorized to manage and confirm details before any cancel, create, or modify request.

Risk: Phone numbers and booking identifiers may be entered in shell commands or temporary files.

Mitigation: Avoid storing real phone numbers or booking IDs in shell history, logs, or reusable files.

Risk: The setup installs an unpinned global npm CLI.

Mitigation: Review the CLI package and installation source before installing, and manage the installed version according to local policy.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command recipes for fpx requests and cautions for real booking changes.]

## Skill Version(s):

0.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
