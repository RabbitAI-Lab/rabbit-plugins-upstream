## Description:

Use when creating an LLM skill from a documentation website URL, including component libraries, API references, and framework guides, with guidance for SPA fallback, token optimization, and packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wufengsheng](https://clawhub.ai/user/wufengsheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to convert documentation websites into reusable LLM skills with structured references, slim trigger instructions, and packaging checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may use web or GitHub access and local file operations while building a skill.

Mitigation: Run it in an appropriate workspace and review generated files before replacing or merging an existing skill.

Risk: Generated documentation skills may contain incorrect, stale, or overly broad guidance if scraped or transformed content is not reviewed.

Mitigation: Review generated skill content, references, and packaging checks before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wufengsheng/skills/create-docs-skill)
- [Publisher profile](https://clawhub.ai/user/wufengsheng)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions with JSON examples, shell command examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow guidance for creating and packaging documentation-derived skills; review generated skill changes before replacing or merging an existing skill.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
