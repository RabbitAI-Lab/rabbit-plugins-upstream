## Description:

Automates WorkBuddy daily credit check-ins by reading the local WorkBuddy login token and calling the documented WorkBuddy check-in API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT-0

## Use Case:

External WorkBuddy users use this skill to run or schedule an idempotent daily check-in that claims WorkBuddy credits from their own logged-in desktop session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a sensitive local WorkBuddy access token and uses it for check-in.

Mitigation: Install only if comfortable with that token access, run manually or on an explicitly configured schedule, and keep terminal output and logs private.

Risk: Optional Electron auto-install and python fallback expand the local trust boundary for older WorkBuddy accounts.

Mitigation: Prefer the Node path for current WorkBuddy releases or manually specify verified runtimes; enable optional Electron auto-install or python fallback only when needed and understood.

Risk: The check-in flow sends the local token to the WorkBuddy API.

Mitigation: Use the skill only for the documented WorkBuddy check-in workflow and confirm network access is limited to the documented WorkBuddy endpoints.

## Reference(s):

- [Dependencies](references/dependencies.md)
- [WorkBuddy website](https://www.codebuddy.cn/work/)
- [WorkBuddy check-in status API](https://copilot.tencent.com/billing/meter/checkin-status)
- [WorkBuddy daily check-in API](https://copilot.tencent.com/billing/meter/daily-checkin)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and scheduling snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local setup, check-in, troubleshooting, and scheduling guidance; scripts may write local check-in result logs without token values.]

## Skill Version(s):

1.0.2 (source: server evidence, frontmatter, CHANGELOG released 2026-08-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
