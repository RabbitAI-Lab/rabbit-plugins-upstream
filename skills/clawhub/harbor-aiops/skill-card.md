## Description:

Governed Harbor registry diagnosis for health, storage, GC, replication and retention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and registry administrators use this skill to diagnose Harbor health, storage, projects, artifacts, scans, vulnerabilities, quotas, garbage collection, replication and retention, and to perform its limited scan and tag maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintenance writes can have uncertain outcomes, and tag deletion has no safe undo.

Mitigation: Use a narrowly scoped Harbor account, review the target and dry-run result, and read current state before retrying an uncertain write.

Risk: The executable package and its credential safeguards are outside this documentation-only bundle.

Mitigation: Verify the executable package and version before supplying Harbor credentials.

## Reference(s):

- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Project homepage](https://github.com/AIops-tools/Harbor-AIops)
- [ClawHub release page](https://clawhub.ai/zw008/skills/harbor-aiops)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration instructions, Operational guidance]

**Output Format:** [Markdown guidance, Harbor diagnostic results, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Probe and write results may be incomplete or unknown; check status fields and verify current state before retrying.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
