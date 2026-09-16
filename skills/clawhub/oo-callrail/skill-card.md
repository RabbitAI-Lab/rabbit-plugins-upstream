## Description:

CallRail (callrail.com). Use this skill for CallRail search and read requests through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read CallRail account, call, company, and form submission data through the OOMOL connector and oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes CallRail data through OOMOL as an intermediary.

Mitigation: Install only if that data path is acceptable for the intended CallRail data and account.

Risk: The first-time setup section includes remote one-line installer commands.

Mitigation: Prefer a pinned, verifiable oo CLI installation method or review the installer before executing it.

Risk: The security verdict is suspicious due to broad data-routing behavior and installer review concerns.

Mitigation: Review the skill and its OOMOL connection requirements before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-callrail)
- [CallRail Homepage](https://www.callrail.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only CallRail connector actions return JSON data through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
