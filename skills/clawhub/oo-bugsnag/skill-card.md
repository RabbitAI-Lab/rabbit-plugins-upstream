## Description:

Bugsnag (bugsnag.com). Use this skill for Bugsnag requests that search and read organizations, projects, errors, events, and releases through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Bugsnag organizations, projects, errors, events, and releases through the oo CLI without handling raw Bugsnag tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute shell or PowerShell scripts.

Mitigation: Review installer commands before use, prefer pinned or signed packages, and verify checksums or signatures where available.

Risk: The skill requires connecting a Bugsnag account through OOMOL before actions can run.

Mitigation: Approve authentication and account-connection steps only when you intend to use an OOMOL-connected Bugsnag account.

## Reference(s):

- [ClawHub Bugsnag skill page](https://clawhub.ai/oomol/skills/oo-bugsnag)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Bugsnag homepage](https://www.bugsnag.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing oo CLI JSON payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
