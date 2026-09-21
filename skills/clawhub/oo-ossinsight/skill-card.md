## Description:

Provides agent access to OSS Insight for GitHub repository analytics through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query OSS Insight for GitHub repository trends, collection rankings, and repository contributor metrics, and to run confirmed ranking actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote install commands for the oo CLI.

Mitigation: Review the CLI setup before installing and prefer a verified or package-manager installation path.

Risk: The rank_collection_repos_by_* actions are documented as write actions and their exact state changes may be unclear before execution.

Mitigation: Fetch the live connector schema and confirm the intended payload and effect with the user before running any rank_* action.

## Reference(s):

- [OSS Insight homepage](https://ossinsight.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ossinsight)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; routine get/list actions are read-oriented, while rank_collection_repos_by_* actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
