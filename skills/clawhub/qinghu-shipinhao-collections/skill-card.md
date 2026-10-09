## Description:

Retrieves the collections published by a WeChat Channels account and provides their topic IDs and types.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents can look up a WeChat Channels account's published collections to identify collection topic IDs and types for follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading unpinned runtime packages can introduce unreviewed code.

Mitigation: Use a trusted, preinstalled, pinned qhkit version and review runtime changes before installation.

Risk: Storing a Qinghu API token locally can expose credentials.

Mitigation: Use an environment variable or a platform-managed secret instead of persistent local storage.

Risk: Collection lookups are paid and may incur unexpected credit charges.

Mitigation: Check the current estimate and obtain user approval before making paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-collections)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise answer with collection topic IDs and types; table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credit consumption for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
