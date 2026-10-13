## Description:

Tracks industry evidence against saved snapshots to produce baseline or change briefings, comparable indicators, opportunity hypotheses, and risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Industry researchers and analysts use this skill to establish evidence baselines or compare new industry reports with prior snapshots, documenting indicator changes, opportunity hypotheses, and risks.

### Deployment Geography for Use:

Global, subject to source access and JishuDB availability.

## Known Risks and Mitigations:

Risk: Bundled setup can download and run JishuDB Desktop software and change local client configuration.

Mitigation: Review the complete installation plan, release, SHA-256, destinations, and configuration target before approval; decline or use an existing or remote JishuDB service if local installation is unwanted.

Risk: Unverified reports or incomparable historical indicators can make opportunity conclusions misleading.

Mitigation: Check source coverage, dates, definitions, and comparability; distinguish observed changes from hypotheses and mark unsupported comparisons as non-comparable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/industry-opportunity-radar)
- [Skill homepage listed in metadata](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/industry-opportunity-radar)
- [Evidence and report discovery contract](references/evidence-contract.md)
- [JishuDB setup guide](references/jishudb-setup/setup.md)
- [199IT report category](https://www.199it.com/archives/category/report)

## Skill Output:

**Output Type(s):** [Markdown briefings, CSV indicator tables, Evidence snapshots and guidance]

**Output Format:** [Markdown and CSV files, with supporting JishuDB records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Initial runs establish a baseline; recurring runs require separate host scheduling authorization.]

## Skill Version(s):

0.1.8 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
