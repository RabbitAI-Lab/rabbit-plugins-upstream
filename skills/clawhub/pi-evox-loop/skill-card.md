## Description:

Helps coding agents recall validated fixes at task start, record fixes they use, and save newly learned repairs for future tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to give coding agents a local memory of reviewed fixes, track when those fixes help, and optionally measure their impact in controlled experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imported or generated fixes may contain unsuitable instructions that an agent later recalls.

Mitigation: Review each fix before approving it for reuse.

Risk: Optional LLM refinement may send transcript content to a configured endpoint.

Mitigation: Leave --llm-refine disabled unless sharing that content with the endpoint is acceptable.

Risk: Optional agent-hook installation changes how future sessions recall fixes.

Mitigation: Inspect the dry-run output before applying installers with --yes.

## Reference(s):

- [Pi EvoX Loop on ClawHub](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)

## Skill Output:

**Output Type(s):** [Text guidance, Shell commands, Configuration guidance, Markdown]

**Output Format:** [Text and Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local fix records and experiment reports.]

## Skill Version(s):

0.19.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
