## Description:

BlazeMeter Performance helps agents read BlazeMeter user, account, workspace, project, test, and performance-test data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and performance teams use this skill to query BlazeMeter Performance resources and inspect performance tests through an OOMOL-connected account. The skill supports read-oriented operational lookup without exposing raw BlazeMeter credentials to the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands that can execute remote code on the user's machine.

Mitigation: Review the oo CLI installation path before use and prefer verified vendor documentation or a signed/package-managed release instead of allowing an agent to run the installer automatically.

Risk: Read-only connector actions can expose BlazeMeter account, workspace, project, user, and test data to the active agent session.

Mitigation: Use the OOMOL-connected account with appropriate access, confirm the intended account or workspace context, and keep credentials server-side rather than passing raw API keys to the agent.

## Reference(s):

- [BlazeMeter Performance homepage](https://www.blazemeter.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-blaze-meter-performance)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; connector runs return data under data and execution metadata under meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
