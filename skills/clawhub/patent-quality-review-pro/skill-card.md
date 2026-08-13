## Description:

Reviews PDF or Word patent application files against a full set of quality indicators, applies domain-specific AHP weighting with user confirmation, uses novelty and non-obviousness checks for stability analysis, and generates a standard two-page Word quality evaluation form.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent professionals, agents, and review teams use this skill to assess application drafting quality, claim stability, specification support, and formatting issues before producing a Word quality review report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads patent and prior-art files that may contain confidential information.

Mitigation: Use approved documents and authorized PatSnap/Open Platform MCP accounts, and run the skill only in workspaces that match the organization's data handling rules.

Risk: The skill can install python-docx and write Word reports, manifests, and final response files.

Mitigation: Review dependencies and generated files before deployment, and run the skill in a controlled agent workspace.

Risk: The Word-generation path may automatically open the output directory on the user's desktop.

Mitigation: Use the no-open option or restrict output paths when automatic desktop opening is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-quality-review-pro)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Issue 9 patch notes](artifact/references/issue9_patch.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON review data, shell commands, and Word/JSON output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a two-page Word evaluation form, output manifest, and final response; the Word-generation path can open the output directory unless disabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
