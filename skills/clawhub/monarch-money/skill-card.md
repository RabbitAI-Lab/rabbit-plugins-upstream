## Description: <br>
TypeScript library and CLI for Monarch Money budget management. Search transactions by date/merchant/amount, update categories, list accounts and budgets, manage authentication. Use when user asks about Monarch Money transactions, wants to categorize spending, needs to find specific transactions, or wants to automate budget tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davideasaf](https://clawhub.ai/user/davideasaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to automate Monarch Money budget tasks, including searching transactions, updating categories and notes, listing accounts and budgets, and managing authentication. It can support both CLI workflows and TypeScript library integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive Monarch Money credentials and MFA secrets. <br>
Mitigation: Prefer environment variables over command-line password or MFA-secret flags, keep debug logging off, and rotate credentials if logs may have captured secrets. <br>
Risk: The skill can make financial-account changes such as updating transaction categories, merchants, notes, and splits. <br>
Mitigation: Review write and delete actions before execution and use a dedicated account setup where possible. <br>
Risk: Saved sessions can grant continued access after login. <br>
Mitigation: Protect local session files and use logout or session deletion when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davideasaf/skills/monarch-money) <br>
- [Monarch Money API Reference](references/API.md) <br>
- [Troubleshooting Guide](references/TROUBLESHOOTING.md) <br>
- [Monarch Money app](https://app.monarchmoney.com) <br>
- [Monarch Money API endpoint](https://api.monarch.com) <br>
- [Monarch Money status](https://status.monarchmoney.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, TypeScript examples, and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May authenticate to Monarch Money and propose or perform financial-account read/write operations when the user runs the CLI or library code.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
