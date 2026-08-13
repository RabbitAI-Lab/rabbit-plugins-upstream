## Description:

Guides an agent through patent-map white-space discovery, problem-value assessment, contradiction diagnosis, and structured resolution ideas with required user confirmation checkpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, R&D strategists, and innovation teams use this skill to identify candidate white-space areas in patent maps, evaluate whether they correspond to valuable unsolved problems, and develop logically grounded contradiction-resolution directions. It is intended for opportunity scouting and analysis, not technical validation, commercial validation, or patent portfolio advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent analysis may involve confidential business strategy or unpublished invention details.

Mitigation: Use only approved PatSnap/Zhihuiya MCP accounts and approved workspaces for confidential data, and avoid entering sensitive information unless those systems are authorized for it.

Risk: The skill saves a local HTML report that may contain sensitive patent or strategy analysis.

Mitigation: Handle generated reports according to the user's confidentiality, retention, and sharing requirements.

Risk: Patent-map sparsity can be mistaken for a validated innovation opportunity.

Mitigation: Treat the output as opportunity-scoping analysis, preserve the skill's false-white-space checks and confirmation gates, and require separate technical, commercial, and patent portfolio validation.

## Reference(s):

- [Candidate white-space evaluation framework](references/evaluation-framework.md)
- [Output templates](references/output-templates.md)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/discover-patent-white-space-opportunities)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown analysis with structured tables and a self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user confirmation gates before deeper analysis; may use configured PatSnap/Zhihuiya MCP patent-data access when available.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
