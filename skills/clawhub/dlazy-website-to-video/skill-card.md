## Description:

Helps turn a website URL into a promotional video, social ad, or product demo using dLazy's hosted website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request website-based promotional videos, social ads, and product demos through a project-based dLazy assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, website URLs, and attached files may be sent to dLazy's hosted service.

Mitigation: Share only material approved for the external service, and confirm ambiguous requests before invoking the skill.

Risk: The required external CLI may be installed globally, and its API key may be saved locally.

Mitigation: Review the CLI before installation, use the pinned npx option if a global install is unwanted, and protect the saved API key.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses stream from a hosted service; video generation is handled by the dLazy workflow.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
