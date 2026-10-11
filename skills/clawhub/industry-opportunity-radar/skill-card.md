## Description:

Tracks industry evidence against saved snapshots to produce comparable indicators, change briefings, opportunity hypotheses, and risk observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Industry analysts and researchers use this skill to establish a market-evidence baseline or compare new findings with saved snapshots, then prepare sourced opportunity hypotheses and risk briefings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill may require installing JishuDB Desktop, granting access, and saving research evidence.

Mitigation: Review and approve the setup and evidence-retention scope before proceeding; decline if installation or persistence is not wanted.

Risk: Recurring runs may continue to collect and save research evidence.

Mitigation: Enable scheduling only with separate, explicit authorization.

Risk: Newly collected reports or incompatible indicators may be mistaken for a measured industry trend.

Mitigation: Compare only compatible observations, cite sources, and label first runs as baselines rather than detected trends.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bowen-aijishu/skills/industry-opportunity-radar)
- [Skill project homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/industry-opportunity-radar)
- [Report discovery and evidence contract](artifact/references/evidence-contract.md)
- [JishuDB setup](artifact/references/jishudb-setup/setup.md)

## Skill Output:

**Output Type(s):** [Markdown briefings, CSV indicator tables, Research guidance]

**Output Format:** [Markdown and CSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source citations and saved evidence snapshots; recurring briefings require separate scheduling authorization.]

## Skill Version(s):

0.1.7 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
