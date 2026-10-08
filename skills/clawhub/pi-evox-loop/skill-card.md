## Description:

Helps coding agents recall reviewed fixes, record fixes learned from difficult failures, and optionally measure their effect in controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to reuse relevant fixes across coding tasks, capture newly learned fixes, and optionally test whether recalled guidance improves subsequent attempts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-derived guidance may be saved and later injected into an agent's system prompt without adequate review.

Mitigation: Disable local auto-approval and audit each recorded fix before approving or recalling it.

Risk: Distilling untrusted or mixed session histories may persist misleading instructions for future tasks.

Mitigation: Review session histories and proposed changes before running distillation with --commit.

Risk: LLM refinement may disclose session content to a configured endpoint.

Mitigation: Use --llm-refine only after checking the endpoint and the session data that may be sent.

Risk: Fresh-start and hook-installation options can change stored memory or host behavior.

Mitigation: Back up stored fixes before --fresh and inspect hook changes before installing them.

## Reference(s):

- [Project homepage](https://github.com/stwhwing/pi-evox-lab)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown and plain-text fix lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Numbered recalled fixes and reusable guidance from recorded failures.]

## Skill Version(s):

0.16.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
