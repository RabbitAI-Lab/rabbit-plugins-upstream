## Description:

YuanShou yotta-publish-guard helps agents and developers run pre-release skill checks, verify packaging and versions, check name availability, and prepare guarded publish commands for GitHub, npm, and ClawHub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and release engineers use this skill before publishing agent skills to run readiness checks, package checks, version alignment checks, name availability checks, and guarded publish command planning. It supports normal release workflows while leaving final publishing decisions and credentialed CLI authentication to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad installation can make the skill available across more agent surfaces than intended.

Mitigation: Choose a specific install target and avoid all-agent installation unless broad availability is intentional.

Risk: Credentialed publish actions can create public repositories or publish packages through locally authenticated CLIs.

Mitigation: Use the default dry-run plan first, review the generated commands, and reserve --exec or --force for explicit release approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-publish-guard)
- [Check items](references/check-items.md)
- [Publish flow](references/publish-flow.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run publish plans, readiness verdicts, version/package findings, and manual follow-up prompts when network checks are unavailable.]

## Skill Version(s):

0.2.2 (source: server release metadata; artifact files still declare 0.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
