## Description:

Helps coding agents recall reviewed fixes at task start, record fixes they use, and save new repairs for future tasks, with optional controlled experiments to measure reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to help coding agents reuse reviewed repairs, save newly discovered fixes, and optionally compare agent performance with and without recalled fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored repair notes or agent history may contain sensitive information.

Mitigation: Review and remove sensitive content before approving repairs in the local asset store.

Risk: Optional hooks and recalled repairs can influence future agent prompts.

Mitigation: Review stored repairs and optional hooks before enabling them, and keep approval gates in place.

Risk: Optional LLM refinement can send transcript content to an external endpoint.

Mitigation: Enable refinement only with a trusted endpoint and after checking what transcript data it receives.

## Reference(s):

- [ClawHub release](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage (listed in ClawHub metadata; import provenance unavailable)](https://github.com/stwhwing/pi-evox-lab)
- [Security and license guidance](docs/security-and-license.md)
- [Using other coding agents](docs/other-agents.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recalled fixes require relevance checks and review before reuse.]

## Skill Version(s):

0.14.7 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
