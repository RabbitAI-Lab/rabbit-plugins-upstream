## Description:

Rollbar (rollbar.com). Use this skill for ANY Rollbar request - searching and reading data. Whenever a task involves Rollbar, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support engineers, and operations teams use this skill to inspect Rollbar projects, items, occurrences, deploys, and environments through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified remote install commands that can execute arbitrary code on a user's machine.

Mitigation: Before installing, review the oo CLI installer source and prefer a signed or package-manager installation path if available.

Risk: Rollbar error data can contain sensitive application details even when actions are read-only.

Mitigation: Connect only Rollbar projects and scopes that are appropriate to expose through OOMOL, and review returned data before sharing it.

## Reference(s):

- [ClawHub Rollbar skill page](https://clawhub.ai/oomol/skills/oo-rollbar)
- [Rollbar homepage](https://rollbar.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Rollbar connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
