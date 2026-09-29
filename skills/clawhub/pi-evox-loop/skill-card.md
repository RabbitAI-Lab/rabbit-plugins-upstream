## Description:

Helps coding agents recall reviewed fixes at task start, record fixes actually used, and save new repairs for future tasks, with optional controlled experiments to measure the benefit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to recall approved repairs for coding tasks, save useful fixes after difficult failures, and optionally compare subsequent runs to assess whether recalled experience helps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored experience can influence future agent responses.

Mitigation: Review proposed fixes before approval, especially in shared or production environments.

Risk: Automatic approval with LLM refinement can admit unsuitable fixes.

Mitigation: Keep manual review enabled unless you accept the risk of automatic approval.

Risk: Distilling OpenClaw or Hermes session databases can expose private session content.

Mitigation: Review the privacy impact before processing session databases.

## Reference(s):

- [ClawHub release](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage (listed in release metadata; import provenance unavailable)](https://github.com/stwhwing/pi-evox-lab)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes recalled repair suggestions and steps for reviewing and saving new fixes.]

## Skill Version(s):

0.14.5 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
