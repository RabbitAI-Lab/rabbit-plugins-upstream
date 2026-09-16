## Description:

Dandelion API routes agent requests for sentiment analysis, semantic text similarity, language detection, and linked entity extraction through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Dandelion text intelligence actions through an OOMOL-connected Dandelion API account without handling raw API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes direct execution of remote oo CLI installer scripts.

Mitigation: Review the official installer instructions, prefer a verified or pinned package when available, and approve installation manually before allowing the skill to run Dandelion actions.

Risk: The skill depends on an OOMOL-connected Dandelion API account and live connector schemas.

Mitigation: Inspect each action schema before constructing payloads and approve account connection or reconnection only when the intended Dandelion API account should be used.

## Reference(s):

- [Dandelion API homepage](https://dandelion.eu/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dandelion)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs Dandelion connector actions through the oo CLI and returns action responses as JSON when invoked with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
