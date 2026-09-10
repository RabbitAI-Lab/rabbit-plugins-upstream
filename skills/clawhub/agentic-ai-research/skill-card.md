## Description:

Searches recent top-conference and journal Agentic AI research using an H=(E,T,C,S,L,V)+P filtering framework, then produces a human-readable literature review and, with confirmation, can compile it into a local wiki.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and technical writers use this skill to run structured Agentic AI literature searches, assess coverage across the H=(E,T,C,S,L,V)+P framework, and produce readable Markdown research summaries. With explicit user confirmation, the skill can also organize the review into a project-local wiki.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional wiki workflow performs project-local file writes and the security summary flags that page metadata can drive Markdown writes outside the intended wiki topics directory.

Mitigation: Use the wiki feature only with trusted wiki content, review generated or edited page frontmatter before running build_index.py, and keep writes scoped to the configured project-local wiki root.

Risk: The skill may suggest optional package installation while performing literature review and wiki workflows.

Mitigation: Run optional pip installation only inside an isolated environment and prefer the lower-risk literature-review-only workflow when wiki compilation is unnecessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/agentic-ai-research)
- [Wiki component boundary README](artifact/README.md)
- [Schema guide](artifact/references/schema-guide.md)
- [Page authoring guide](artifact/references/page-authoring.md)
- [Cascade update workflow](artifact/references/cascade-update.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown literature review with optional project-local wiki Markdown files and JSON index reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional wiki writes require explicit user confirmation and are scoped to the configured project-local wiki root.]

## Skill Version(s):

1.1.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
