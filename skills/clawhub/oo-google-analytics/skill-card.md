## Description:

Google Analytics helps an agent operate Google Analytics through an OOMOL-connected account, including reporting, account and property discovery, metadata lookup, quota inspection, and selected property configuration updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to let an agent query Google Analytics accounts, properties, reports, metadata, and quotas through an OOMOL-connected Google Analytics account. It also supports guarded write actions for custom dimensions, custom metrics, data retention, and property settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute local code.

Mitigation: Treat setup as high-trust local code execution; prefer an official package manager or separately download, inspect, and verify the installer before running it.

Risk: Some actions can change Google Analytics custom definitions, data retention, or property settings.

Mitigation: Confirm the exact Google Analytics property, action, and payload with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-google-analytics)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Google Analytics](https://analytics.google.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Analytics Icon](https://static.oomol.com/logo/third-party/google_analytics.svg)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
