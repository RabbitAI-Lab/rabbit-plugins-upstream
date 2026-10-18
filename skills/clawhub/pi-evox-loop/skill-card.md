## Description:

Helps coding agents recall reviewed fixes at task start, record when they are used, and save useful repairs for future tasks, with optional controlled experiments to assess the benefit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to carry reviewed fixes across coding tasks, track when prior fixes help, and optionally compare outcomes in controlled repeat runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored experience can influence future coding-agent prompts, including in sensitive projects.

Mitigation: Review saved fixes before approving them and retain human oversight of the advice an agent applies.

Risk: Optional LLM refinement may send transcript excerpts to a configured endpoint.

Mitigation: Leave --llm-refine disabled unless the configured endpoint and transcript sharing are acceptable.

Risk: Optional hook or snippet installation changes agent integration files.

Mitigation: Check the exact target files before enabling install-hooks or install-snippet.

## Reference(s):

- [Pi EvoX Loop on ClawHub](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage (listed in ClawHub metadata)](https://github.com/stwhwing/pi-evox-lab)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recall suggestions draw on locally stored, reviewed experience records.]

## Skill Version(s):

0.22.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
