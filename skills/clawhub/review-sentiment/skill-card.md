## Description:

Analyzes Amazon review sentiment by theme so sellers can understand positive and negative patterns, review evidence, trends, and improvement opportunities for an ASIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to ask an agent for ASIN-level review sentiment analysis, VOC reports, competitor comparison, alerts, monitoring guidance, and exports based on ARI data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits automatically under server rules.

Mitigation: Configure the ARI account to ask before every paid operation or use only explicit quote-only requests when cost approval is required.

Risk: Monitoring or schedule changes can lead to ongoing review collection and future credit use.

Mitigation: Approve monitoring or schedule changes only when ongoing collection is intended and review the cost note before enabling a recurring cadence.

Risk: Exported files can overwrite local files.

Mitigation: Run exports from a dedicated empty folder rather than a home directory or active project directory.

Risk: The skill needs access to an ARI account and review data.

Mitigation: Install only when the user is comfortable granting that access and avoid placing ARI API keys in chat, reports, or command examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-sentiment)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Usage guide](artifact/README.md)
- [Detailed user guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Natural-language answers and Markdown reports, with optional shell commands and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on ARI-collected Amazon review data and may include sample scope, review evidence, trends, report links, credit-use notes, and limitations when data is insufficient.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
