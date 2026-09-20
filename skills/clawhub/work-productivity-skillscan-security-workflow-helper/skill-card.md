## Description:

Helps agent users, skill authors, maintainers, and teams turn SkillScan-style security and reliability needs into practical workflows, checklists, analyses, code changes, and decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to adapt popular SkillScan-style patterns into practical local workflows for bug fixing, setup hardening, safety review, reliability improvement, and adjacent skill creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation can route unrelated security, bug-fix, or workflow requests through this helper.

Mitigation: Prefer explicit invocation or narrower triggers in sensitive environments, and review the skill scope before installation.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper)
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter)
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan)
- [Popular ClawHub skill demand: AdMapix](https://clawhub.ai/skills/admapix)
- [Popular ClawHub skill demand: PollyReach](https://clawhub.ai/skills/pollyreach)
- [Security review: permission and message-boundary audit](https://github.com/OPP-studio-macchino/chatgpt-completion-sound/issues/2)
- [Add consent-gated anonymous product analytics](https://github.com/Misiek22113/ReviewGuard/issues/1)
- [Unbounded Cloud Monitoring pagination can exhaust plugin memory for large distribution queries](https://github.com/grafana/grafana-cloudmonitoring-datasource/issues/121)
- [Standard text editing in the ZeroCode composer](https://github.com/zeroclaw-labs/zeroclaw/issues/10909)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text with optional code blocks, shell commands, configuration snippets, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, limits, validation performed, and remaining risks when relevant.]

## Skill Version(s):

0.20260916.221748 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
