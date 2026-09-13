## Description:

NinjaTrader 8 NinjaScript development reference for using directives, lifecycle patterns, indicators, order management, compile errors, and deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmdeep](https://clawhub.ai/user/gmdeep)

### License/Terms of Use:

MIT

## Use Case:

Developers and trading automation engineers use this skill to draft, validate, debug, migrate, and deploy NinjaTrader 8 NinjaScript strategies and indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fixed SSH/SCP deployment commands may send strategy source code to a maintainer-specific remote host and path.

Mitigation: Require explicit user approval of the host, remote account, destination path, and file before any SSH or SCP command is run.

Risk: Deployment instructions include environment-specific values that may not match the user's NinjaTrader installation.

Mitigation: Replace fixed deployment values with user-provided placeholders and confirm them before writing or transferring files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gmdeep/skills/ninjatraderopenclawskill)
- [Source repository](https://github.com/GMDEEP/NinjatraderOpenClawSkill)
- [Release history](https://github.com/GMDEEP/NinjatraderOpenClawSkill/releases)
- [Publisher profile](https://clawhub.ai/user/gmdeep)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with C# code blocks, checklists, tables, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes NinjaScript templates, compile-error mappings, validation checklists, migration notes, and deployment steps.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
