## Description:

Audits a repository's documentation governance, installs optional checks and hooks, and detects discrepancies between documentation and implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to assess documentation governance, install repository checks with explicit confirmation, and identify outdated or inconsistent documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installed documentation gates can persist and block commits or new plans.

Mitigation: Run init without --yes first, review the proposed repository and hook changes, and remove installed hooks and settings entries if they are too intrusive.

## Reference(s):

- [docs-gov on ClawHub](https://clawhub.ai/xiaoba-dev/skills/docs-gov)
- [Documentation governance framework](framework.md)
- [Incidents behind the checks](incidents.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and plain-text diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confirmed installation can create repository configuration, scripts, templates, and hooks.]

## Skill Version(s):

2.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
