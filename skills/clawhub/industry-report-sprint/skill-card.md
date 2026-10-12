## Description:

Researches a sector and produces a source-cited industry report, product comparison, and evidence trail, retaining research and revisions in JishuDB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and decision-makers use this skill to turn a sector name into a written market brief with cited evidence, representative product comparisons, competitive analysis, and explicit information gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Required JishuDB setup can install a local Desktop app and change the agent client's connection settings.

Mitigation: Review the redacted installation plan, release source, destination, endpoint, and client changes before approving setup.

Risk: Research sources or stored reports may include restricted or sensitive material.

Mitigation: Use authorized sources and a consented JishuDB destination; do not put private documents in public searches or share tokens and OAuth codes in chat.

## Reference(s):

- [Skill homepage (listed in metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/industry-report-sprint)
- [Report discovery and evidence contract](references/evidence-contract.md)
- [JishuDB setup guide](references/jishudb-setup/setup.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, CSV]

**Output Format:** [Source-cited Markdown report and comparisons, evidence CSV, source list, and revision notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires JishuDB records for research evidence, drafts, final text, and revisions.]

## Skill Version(s):

0.1.8 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
