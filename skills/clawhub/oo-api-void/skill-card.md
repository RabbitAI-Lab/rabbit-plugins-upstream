## Description:

APIVoid connector skill for domain, IP, URL, and email checks, plus APIVoid account usage lookups through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to inspect APIVoid connector schemas and run reputation checks, email verification, and account usage requests from an agent environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell and PowerShell installer snippets for the OOMOL oo CLI.

Mitigation: Prefer an official, version-pinned installer or package manager flow with checksum or signature verification, and avoid running remote installer pipelines from an elevated session.

## Reference(s):

- [APIVoid homepage](https://www.apivoid.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub APIVoid skill page](https://clawhub.ai/oomol/skills/oo-api-void)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first oo CLI execution; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
