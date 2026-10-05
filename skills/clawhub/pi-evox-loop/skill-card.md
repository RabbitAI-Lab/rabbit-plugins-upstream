## Description:

Helps coding agents recall reviewed fixes at task start, record fixes that prove useful, and save new repairs for future tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to carry reviewed troubleshooting fixes across coding-agent sessions and optionally measure their effect in controlled experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-session content may be stored persistently and reused across projects.

Mitigation: Scope EVOX_STORE_DIR and EVOX_HITS_DIR by project; do not connect private session databases unless their contents are approved for storage.

Risk: Stored fixes can enter future agent prompts, including unhelpful or unsafe instructions if approved without review.

Mitigation: Keep manual review enabled, especially in shared or production environments; avoid auto-approval.

Risk: Optional LLM refinement can process session contents at a configured endpoint.

Mitigation: Use a refinement endpoint only when authorized to share or process the session contents there.

## Reference(s):

- [Project homepage (listed for this release)](https://github.com/stwhwing/pi-evox-lab)
- [ClawHub skill listing](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Security and license guidance](docs/security-and-license.md)
- [Other agent integrations](docs/other-agents.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and command-line output describing relevant fixes, their use, and experience-store updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reviewed fixes may be recalled across sessions; optional experiments produce comparisons of agent runs.]

## Skill Version(s):

0.14.8 (source: server release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
