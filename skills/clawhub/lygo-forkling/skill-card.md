## Description:

LYGO Forkling is a local test-agent skill that creates a fork under CHAMPION_LYRA, runs claim-gated task loops, snapshots generations locally, and prints dry-run Star Chart proposal JSON without live ingest or git push.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run a local self-improving test-agent loop that writes consent-gated state, checks claims, and prepares dry-run proposal JSON for later human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and updates local state files while running a test-agent loop.

Mitigation: Run write-capable commands only with explicit --i-consent and review generated state before using it elsewhere.

Risk: Dry-run proposal JSON could be mistaken for an approved live Star Chart change.

Mitigation: Treat propose output as pending review only; use a separate human-reviewed ingest or publishing process for any live change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-forkling)
- [ClawHub metadata link](https://clawhub.ai/deepseekoracle/lygo-forkling)
- [Homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-forkling)
- [Security notes](references/SECURITY.md)
- [SkillSpector audit notes](references/SKILLSPECTOR_AUDIT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with shell commands, local state files, and dry-run JSON proposal output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local state only with explicit --i-consent; propose prints JSON and does not perform live chart ingestion.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
