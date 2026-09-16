## Description:

Retrieves WakaTime coding time, stats, summaries, projects, status bar data, and current user details through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to query WakaTime account data from an agent, including coding stats, daily summaries, projects, status bar information, and account details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup suggests piping mutable remote installer scripts into a shell.

Mitigation: Prefer official package-manager or verified installer instructions, inspect downloaded scripts before execution, and avoid elevated privileges.

Risk: Live WakaTime calls depend on a correctly installed oo CLI, OOMOL sign-in, and connected WakaTime account.

Mitigation: Run setup steps only after an auth, connection, CLI, or billing error, and keep WakaTime credentials in server-side connection handling.

## Reference(s):

- [ClawHub WakaTime Skill Page](https://clawhub.ai/oomol/skills/oo-wakatime)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [WakaTime Homepage](https://wakatime.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [WakaTime Icon Asset](https://static.oomol.com/logo/third-party/WakaTime.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text responses with optional shell commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected WakaTime account for live connector calls.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
