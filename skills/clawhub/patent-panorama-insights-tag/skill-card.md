## Description:

This skill helps patent panorama teams design a structured patent tagging taxonomy, key technical questions, recommended patent-family packages, a small tagged demonstration sample, and export files for downstream SaaS tagging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External patent analysis teams use this skill after candidate-pool search, human SaaS tagging, and statistical analysis are complete. It turns those inputs into a validated taxonomy proposal, key questions, recommended patent packages, demonstration tagging records, and an export for full tagging in the customer's SaaS tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow stage sequencing can be confusing, especially whether the skill runs before or after full SaaS tagging.

Mitigation: Confirm that tagged_pool.csv, tech_taxonomy.txt, panorama_stats.json, and value_signals.json are available before using the skill.

Risk: Patent data may be confidential when sent through the configured MCP service or downstream SaaS tagging workflow.

Mitigation: Check organizational confidentiality rules and data-transfer approvals before processing patent records.

Risk: The generated taxonomy and patent-package recommendations may be mistaken for legal review or exhaustive patent analysis.

Mitigation: Use the outputs as structured tagging guidance and require reviewer validation for legal, commercial, or filing decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-panorama-insights-tag)
- [Open Platform marketplace listing](https://open.zhihuiya.com/marketplace/skill-hub/patent-panorama-insights-tag)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [JSON, CSV, Markdown, and optional HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces tech_breakdown.json, key_questions.json, patent_packages.csv, tagging_demo_sample.csv, to_be_tagged.csv, taxonomy_proposal.md, and optionally panorama_stats_report.html under @session/pps-output/.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
