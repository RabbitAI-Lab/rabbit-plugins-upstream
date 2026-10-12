## Description:

Helps coding agents recall reviewed fixes, record when they help, and save new repairs for future tasks, with optional controlled experiments to measure results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to give coding agents access to reviewed repairs at task start and preserve useful fixes after difficult failures. Optional controlled experiments can evaluate whether remembered fixes improve subsequent runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent remembered fixes can influence future agent behavior, including through harmful instructions in imported or shared entries.

Mitigation: Review imported and shared entries before approving them, and verify recalled fixes before use.

Risk: Optional language-model refinement can send session transcripts to the configured endpoint.

Mitigation: Leave --llm-refine disabled unless you consent to sending those transcripts to that endpoint.

Risk: Installing hooks or instruction snippets can change how agents behave in later sessions.

Mitigation: Use the dry-run modes and review proposed changes before allowing hook or instruction-file writes.

## Reference(s):

- [Pi EvoX Loop on ClawHub](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Security and license guidance](artifact/docs/security-and-license.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recalled fixes are suggestions to review before applying.]

## Skill Version(s):

0.18.1 (source: ClawHub release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
