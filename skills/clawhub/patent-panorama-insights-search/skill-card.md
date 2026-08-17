## Description:

Builds expert patent panorama search configurations with topic anchors, noise filters, branch validation, and downstream-ready candidate and taxonomy files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts and IP teams use this skill to start a patent panorama project by translating a topic into validated branch searches, a deduplicated candidate pool, lightweight core recall, and a technology taxonomy for downstream statistics and tagging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential patent search topics may be included in run_config.json or processed through the authorized PatSnap/Zhihuiya integration.

Mitigation: Use only approved projects with the integration, and review run_config.json before retrieval when the project topic is confidential.

Risk: Patent search results and patent-number outputs depend on the connected platform data and the validated branch queries.

Mitigation: Keep the skill's branch precision checks and recall sanity checks in the workflow before handing outputs to downstream analysis.

## Reference(s):

- [Query and Taxonomy Methodology](references/query-and-taxonomy-methodology.md)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-panorama-insights-search)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [PatSnap Open Platform marketplace entry](https://open.zhihuiya.com/marketplace/skill-hub/patent-panorama-insights-search)

## Skill Output:

**Output Type(s):** [Files, Configuration, Analysis, Guidance]

**Output Format:** [JSON, CSV, plain text taxonomy, and concise status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces run_config.json, search_config.json, candidate_pool.csv, core_recall.csv, tech_taxonomy.txt, and report_manifest.json for downstream patent panorama workflow stages.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
