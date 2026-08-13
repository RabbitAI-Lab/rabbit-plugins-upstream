## Description:

Designs a patent panorama tagging taxonomy, key technical questions, recommended patent packages, demo tagged records, and CSV handoff files for downstream SaaS full tagging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts and IP strategy teams use this skill after candidate-search and statistics stages to turn tagged patent pools and value signals into a constrained taxonomy, recommendation packages, demo labels, and handoff files for client SaaS tagging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow order is ambiguous between creating to_be_tagged.csv before SaaS tagging and consuming tagged_pool.csv after SaaS tagging.

Mitigation: Confirm the intended stage and required input files with the publisher before installation or execution.

Risk: MCP or SaaS credentials may be required for the intended patent data workflow.

Mitigation: Configure credentials only in the intended agent environment and avoid exposing them to unrelated tools or sessions.

Risk: Taxonomy and patent-package recommendations can affect downstream patent analysis decisions.

Mitigation: Have patent or domain reviewers check generated classifications, recommendation reasons, and sample labels before client use.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files, JSON, CSV, Markdown, Guidance]

**Output Format:** [Structured files and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces taxonomy, key-question, patent-package, demo-sample, full-export, and proposal artifacts; optional HTML report generation is user-confirmed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
