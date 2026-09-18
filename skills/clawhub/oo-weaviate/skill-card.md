## Description:

Use this skill for Weaviate requests that search, read, and inspect data through the OOMOL Weaviate connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Weaviate action schemas and run read-focused collection, object, and instance metadata operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands for the oo CLI.

Mitigation: Do not let an agent automatically run the installer; review the installer path and prefer a verified release or package manager before using the skill.

## Reference(s):

- [ClawHub Weaviate skill](https://clawhub.ai/oomol/skills/oo-weaviate)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Weaviate homepage](https://weaviate.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schema responses before action execution.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
