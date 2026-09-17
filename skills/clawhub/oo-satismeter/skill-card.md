## Description:

Use this SatisMeter skill for requests that search and read project, survey, statistics, and response data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live SatisMeter connector schemas and run read-oriented SatisMeter actions through the oo CLI. It supports retrieving projects, surveys, survey statistics, and response lists from an OOMOL-connected SatisMeter account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of remote installer scripts.

Mitigation: Use a verified package-manager or documented safer install path for the oo CLI where possible; if a script must be used, review it before execution.

Risk: SatisMeter requests are handled through OOMOL's connector service.

Mitigation: Confirm that routing SatisMeter data through OOMOL is acceptable for the user's account, data sensitivity, and organizational policy before use.

Risk: Connector payloads can drift from documented action examples.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing or running any action payload.

## Reference(s):

- [SatisMeter homepage](https://satismeter.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SatisMeter icon](https://static.oomol.com/logo/third-party/Satismeter.svg)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-satismeter)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before running actions and to return oo CLI JSON responses when actions are executed.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
