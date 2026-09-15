## Description:

AgentQL lets agents query webpages, create AgentQL Tetra browser sessions, and review usage through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate AgentQL through OOMOL: extracting structured data from webpages, creating remote browser sessions, and checking account or session usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of a remote installer script.

Mitigation: Review the installer path before use and prefer a verified package, pinned release, checksum, or signature verification.

Risk: The skill can create AgentQL browser sessions through a write action.

Mitigation: Confirm the exact action payload and expected effect with the user before running any AgentQL write action.

## Reference(s):

- [AgentQL homepage](https://www.agentql.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [AgentQL skill on ClawHub](https://clawhub.ai/oomol/skills/oo-agentql)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AgentQL connector responses containing structured JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
