## Description:

Helps coding agents recall vetted fixes, record when they help, and save new repairs for future tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use this skill to recall approved repair tips at task start, record successful reuse, and deposit fixes after resolving difficult failures. Optional controlled experiments compare performance with and without recalled fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored repair tips can influence future agent behavior through persistent prompts.

Mitigation: Review approved tips before relying on them and leave shared or imported tips quarantined unless the pool is trusted.

Risk: Optional transcript refinement may disclose private session contents to an external model endpoint.

Mitigation: Avoid --llm-refine for private transcripts unless the endpoint is under your control.

Risk: Installing hooks or snippets can change agent behavior across tasks.

Mitigation: Inspect install-hooks or install-snippet dry-runs before applying --yes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Provider setup](docs/providers.md)
- [Other agent integrations](docs/other-agents.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations may draw on locally stored, approved repair tips.]

## Skill Version(s):

0.17.0 (source: release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
