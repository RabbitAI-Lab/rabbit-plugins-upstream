## Description:

Orchestrates AI-assisted novel writing and GitHub-based serialization across world-building, character design, chapter drafting, continuity verification, and GitHub publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

GPL-3.0 for skill infrastructure; CC-BY-NC-SA-4.0 for generated novel content

## Use Case:

External authors and developers use this skill to plan, draft, validate, and publish serialized novels in GitHub-backed workflows. It helps maintain story state, chapter structure, continuity checks, and release conventions across multi-session writing projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The GitHub publishing setup asks for broader write permissions than needed.

Mitigation: Review the workflow before installation and remove unnecessary packages: write permission.

Risk: Publishing actions can tag, push, or create releases in a repository that may be public.

Mitigation: Require explicit user confirmation before any tag, push, or release action.

Risk: Broad activation triggers may start the skill during casual writing requests.

Mitigation: Confirm the user's intent before invoking the full writing or publishing workflow.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/JohnSmithfan/Novel-Serialization-Skill)
- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/novel-serialization-skill)
- [Method Patterns](references/method-patterns.md)
- [Glossary](references/glossary.md)
- [Prompt Usage Guide](prompts/README.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown documents, YAML frontmatter, Git/GitHub workflow commands, and structured writing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated novel content follows the requested output language; infrastructure and metadata remain in English.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact metadata version 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
