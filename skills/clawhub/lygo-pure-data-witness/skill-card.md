## Description:

Teaches agents to register URLs or local files into the LYGO Pure-Data Witness workflow using a portal pack and consent-gated CLI to create digest records, ledger updates, and Star Chart submission JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to archive public HTTPS pages or local files as Pure-Data Witness digests, produce witness artifacts, rebuild local ledgers, and prepare consent-gated Star Chart submission JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence reports that one included command path can fetch and persist web content without the consent flag promised by the skill.

Mitigation: Prefer the documented pdw_cli.py commands with --i-authorize-fetch and --i-consent; avoid direct scripts/pure_data_witness.py fetch or all paths until consent checks are made consistent.

Risk: A local archive or HF export pack may contain sensitive text because redaction is heuristic and incomplete.

Mitigation: Do not archive private dashboards, cookies, API keys, or other secrets; review generated .txt and .json files before sharing or any third-party publication.

Risk: The skill can fetch public HTTPS pages and write local witness artifacts.

Mitigation: Use only operator-approved HTTPS URLs, keep SSRF and content gates enabled, and write outputs to an intentional review directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-pure-data-witness)
- [ClawHub publisher profile](https://clawhub.ai/user/deepseekoracle)
- [Clawdis homepage link](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/clawhub/mirrors/lygo-pure-data-witness)
- [Register portal](https://deepseekoracle.github.io/lygo-protocol-stack/data-vault/register.html)
- [Pure-Data UI](https://deepseekoracle.github.io/lygo-protocol-stack/data-vault/pure-data.html)
- [Security notes](references/SECURITY.md)
- [SkillSpector audit response](references/SKILLSPECTOR_AUDIT.md)
- [Portal training](references/PORTAL_TRAINING.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON artifact paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write witness cards, snapshots, egg fragments, ledgers, and Star Chart submission JSON under an operator-selected output directory; the skill does not upload or publish artifacts.]

## Skill Version(s):

1.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
