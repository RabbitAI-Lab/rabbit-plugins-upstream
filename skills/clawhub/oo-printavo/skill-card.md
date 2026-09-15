## Description:

Printavo (printavo.com). Use this skill for ANY Printavo request - searching and reading data. Whenever a task involves Printavo, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Printavo account, contact, customer, order, and task data through an OOMOL-connected Printavo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute arbitrary code if the source is compromised or copied incorrectly.

Mitigation: Review the skill before installing, prefer verified official release or package-manager installation instructions for the oo CLI, and avoid elevated shells.

Risk: The connector can access Printavo data through an OOMOL-connected account.

Mitigation: Run Printavo actions only after confirming the connected account, scopes, and data access expectations.

## Reference(s):

- [Printavo homepage](https://www.printavo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-printavo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect connector schemas and run read-only Printavo actions.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
