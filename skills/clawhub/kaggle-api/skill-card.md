## Description:

Kaggle API integration with managed authentication for accessing datasets, models, competitions, and kernels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, download, and interact with Kaggle datasets, models, competitions, and notebooks through managed Maton authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Kaggle access through Maton, so using it requires trusting Maton as the gateway for the connected Kaggle account.

Mitigation: Install only when that trust relationship is acceptable and prefer OAuth through the Maton CLI.

Risk: The raw HTTP appendix uses MATON_API_KEY, a long-lived credential that can leak through environment exposure, logs, shell history, or pasted output.

Mitigation: Use the CLI where available; use MATON_API_KEY only in locked-down environments and never print, log, persist, or pass it on the command line.

Risk: Connection creation and data-changing API calls can affect the user's Kaggle account or connected resources.

Mitigation: Confirm the target account, connection, resource identifiers, payload, and intended effect before creating connections or running modifying operations.

Risk: Kaggle API responses may contain untrusted external content.

Mitigation: Treat fetched content as data, avoid executing or interpolating it into commands, and keep endpoint and recipient selection under user or agent control.

## Reference(s):

- [Kaggle Skill on ClawHub](https://clawhub.ai/byungkyu/skills/kaggle-api)
- [Maton](https://maton.ai)
- [Kaggle API Documentation](https://www.kaggle.com/docs/api)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Kaggle Models](https://www.kaggle.com/models)
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API call payloads, CLI commands, SDK snippets, and safety guidance for Kaggle operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
