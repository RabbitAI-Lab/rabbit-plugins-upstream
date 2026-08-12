## Description:

Looks up LCA emission factors and carbon footprint data from 18 life-cycle inventory databases and 24,000+ published EPDs for material, product, BOM, benchmarking, and EPD review tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kirbyingithub](https://clawhub.ai/user/kirbyingithub)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and LCA practitioners use this skill to retrieve and compare emission factors, carbon footprint data, EPD peer distributions, and benchmark percentiles from HiQ Cortex while preserving database basis and comparability notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Material names, BOM lines, or user wording may be sent to HiQ's remote service during searches.

Mitigation: Redact confidential product, supplier, customer, recipe, and process identifiers before use, and use only approved data with a limited account or key where possible.

Risk: The release security summary says the skill under-discloses that raw user wording and BOM lines are sent to HiQ's remote service.

Mitigation: Review the privacy posture before installation and disclose the remote-query behavior to users who may provide confidential LCA inputs.

Risk: LCA values can be misleading when compared across different databases, functional units, system models, or system boundaries.

Mitigation: Use the skill's comparability notes and require database, version, system model, geography, and reference unit beside every numeric result.

## Reference(s):

- [HiQ Cortex skill page](https://clawhub.ai/kirbyingithub/skills/hiq-cortex)
- [HiQ agent skills repository](https://github.com/HiQ-AI/agent-skills)
- [HiQ LCA data service](https://www.hiqlcd.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with shell commands, JSON snippets, and LCA dataset basis details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON when commands use --json; numeric results should include database, version, system model, geography, and reference unit.]

## Skill Version(s):

1.8.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
