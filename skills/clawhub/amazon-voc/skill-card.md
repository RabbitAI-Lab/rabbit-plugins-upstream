## Description:

Amazon Review Intelligence Extractor helps agents use ARI to collect and analyze Amazon reviews into voice-of-customer reports, consumer insights, competitor comparisons, and listing optimization recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to collect Amazon review data for ASINs and turn it into VOC analysis, pain-point summaries, purchase drivers, user personas, trend reports, competitor comparisons, and listing improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI API keys could be exposed if copied into prompts, reports, screenshots, or shared command examples.

Mitigation: Configure only a private account key through ARI_API_KEY or the local configure command, and keep keys out of reports and command examples.

Risk: Paid review collection or AI analysis can consume ARI credits.

Mitigation: Review the quoted credit cost first and approve only commands that intentionally include --confirm.

Risk: Small or incomplete review samples can lead to overconfident business recommendations.

Mitigation: Use the skill's sample-size warnings and separate direct API data, inferred findings, and strategic recommendations in generated reports.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Server-resolved GitHub provenance](https://github.com/funewa/Amazon-VOC)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/amazon-voc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON CLI responses, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection and AI analysis actions are previewed with quotes and require explicit --confirm before credits are used.]

## Skill Version(s):

1.4.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
