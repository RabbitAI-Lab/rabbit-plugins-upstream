## Description:

Skill Registry provides a local OpenClaw skill registry with trigger-word routing for organizing workspace skills and matching user requests by keyword.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slim-rush](https://clawhub.ai/user/slim-rush)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace maintainers use this skill to list local OpenClaw skills, maintain a central registry, and route user requests to matching skills through configured trigger words.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent trigger-based routing can auto-load other skills from broad trigger words without strong user control.

Mitigation: Prefer explicit commands such as /skills, require confirmation before executing matched skills, and avoid broad triggers for skills that can read private files, use credentials, access the network, or change state.

Risk: A local registry may expose the list of installed workspace skills.

Mitigation: Install only in workspaces where exposing the installed skill list is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/slim-rush/skills/skill-registry)
- [REGISTRY.template.md](artifact/REGISTRY.template.md)
- [RULES.snippet.md](artifact/RULES.snippet.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Guidance]

**Output Format:** [Markdown documents and routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes bilingual English and Chinese registry and routing templates.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
