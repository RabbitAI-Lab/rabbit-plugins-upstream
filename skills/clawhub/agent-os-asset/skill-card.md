## Description:

Design and execute privacy-safe historical-file modernization as a vendor-neutral Agent Skills suite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lee-agi](https://clawhub.ai/user/lee-agi)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and knowledge-base maintainers use this skill to inventory mixed historical folders, create reviewable Agent Asset entries, apply lifecycle decisions, and build final non-PII retrieval indexes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and reorganize files within a selected local folder.

Mitigation: Start with preview or dry-run modes, inspect decision JSON and apply reports, and execute changes only for a trusted scope.

Risk: Automatic sync, delete/apply, indexing, localhost apply, and remote model features can affect local files or send bounded data when explicitly enabled.

Mitigation: Keep those features disabled until needed, confirm the adapter path and scope, and enable only the specific execution gate required for the task.

Risk: Indexes and remote model features could expose sensitive material if PII controls are bypassed.

Mitigation: Use the documented PII exclusions, index only reviewed final non-PII assets, and provide remote credentials only for explicit opt-in features.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lee-agi/skills/agent-os-asset)
- [README](README.md)
- [Agent OS Asset Skill Definition](SKILL.md)
- [Agent Readable Doc Conversion Workflow](skills/agent-readable-doc/references/conversion-workflow.md)
- [KB Review Workflow](skills/kb-review/references/workflow.md)
- [KB Review Output Specification](skills/kb-review/references/output-spec.md)
- [Second Brain Privacy Rules](skills/second-brain/references/privacy.md)
- [Second Brain Update Workflow](skills/second-brain/references/update-workflow.md)
- [Agent Asset Federation](skills/second-brain/references/asset-index-federation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, JSONL, text reports, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated for local review workflows and final non-PII indexing after explicit user-controlled gates.]

## Skill Version(s):

0.1.0 (source: SKILL.md metadata, pyproject.toml, package.json, and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
