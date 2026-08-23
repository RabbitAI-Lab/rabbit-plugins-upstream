## Description:

Scans local AI coding CLIs, checks account and model availability through tiered evidence, and writes a model inventory with routing chains for downstream agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent-workflow maintainers use this skill to discover installed AI coding CLIs, verify which accounts and models are actually usable, and cache routing information for planner, coder, scout, reviewer, and fixer roles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill checks for local AI CLI binaries, auth/config files, and API-key environment variable names.

Mitigation: Install only when local CLI inventory scanning is acceptable, and review the disclosed scan behavior before running it.

Risk: Full scans may run small live model probes unless the user requests a quick scan.

Mitigation: Use quick scan when live probes are not desired, and review probe results before relying on routing decisions.

Risk: The resulting local inventory is saved under ~/.claude/model-inventory.json for other skills to consume.

Mitigation: Review the cached inventory and remove it if downstream agent routing should not use the discovered model availability.

## Reference(s):

- [CLI Registry](references/cli-registry.md)
- [ClawHub Skill Page](https://clawhub.ai/dennisrongo/skills/model-inventory)
- [Publisher Profile](https://clawhub.ai/user/dennisrongo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report plus JSON inventory written to ~/.claude/model-inventory.json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The inventory records CLI installation, auth evidence, model status, probe evidence, and role routing chains.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
