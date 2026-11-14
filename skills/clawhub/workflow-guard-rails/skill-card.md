## Description:

Wraps multi-step agent workflows with seven safeguards for pre-execution checks, checkpoints, side effects, retries, validation, audit logs, and confirmed failure-rule accumulation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to add checks, recovery controls, and audit practices to recurring or multi-step agent workflows that take external actions or must be safe to rerun.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports that setup may replace persistent global guidance with downloaded content without the stated review safeguards.

Mitigation: Consider the suspicious assessment before installing; review and verify the pinned playbook file before allowing workflows to rely on it.

## Reference(s):

- [Guardian Patterns](references/guardian-patterns.md)
- [Pinned companion error playbook](https://raw.githubusercontent.com/haiyangchenbj/error-playbook/d945aee01384c6163beb287446147ce768d50661/ERROR-PLAYBOOK.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown workflow instructions and Guardian Reports, with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven workflow guards; protection applies to actions routed through the side-effect queue.]

## Skill Version(s):

1.0.8 (source: frontmatter; server release 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
