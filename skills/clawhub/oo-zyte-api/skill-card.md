## Description:

Zyte API enables agents to use an OOMOL-connected Zyte API account to extract articles, page content, product data, and browser-rendered HTML from public URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Zyte API connector schemas, run supported extraction actions through the oo CLI, and handle setup issues only when authentication, connection, or billing errors occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to execute a remote installer directly in a shell.

Mitigation: Review the skill before installing; prefer manually downloading and verifying the installer or using an official package manager if available.

Risk: OOMOL processes Zyte request payloads for this connector workflow.

Mitigation: Avoid sending secrets, credentials, private URLs, or confidential data in connector payloads unless that use has been approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zyte-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Zyte API homepage](https://www.zyte.com/zyte-api/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; Zyte responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
