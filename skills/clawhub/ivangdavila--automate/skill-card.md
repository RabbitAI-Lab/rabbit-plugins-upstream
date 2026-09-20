## Description:

Automate helps agents identify repetitive, deterministic tasks that waste tokens and turn them into reusable scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers, engineers, and agent operators use this skill to decide when scripted automation is more appropriate than LLM prompting and to draft repeatable automation patterns for data transformation, validation, file operations, API calls, Git workflows, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable templates may change files, retrieve credentials, make network requests, or publish Git changes without enough guardrails.

Mitigation: Treat templates as unsafe drafts: add dry-runs and confirmations, inspect git status before pushing, avoid automatic credential retrieval, pin npx dependencies, and restrict network requests to trusted destinations.

Risk: Automation proposals may turn incorrect assumptions into repeatable scripts.

Mitigation: Review generated scripts before deployment, scan them for security issues, and test them on representative inputs before routine use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/automate)
- [Automation signals](artifact/signals.md)
- [Script templates](artifact/templates.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with script and shell-command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or draft automation scripts that require review before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
