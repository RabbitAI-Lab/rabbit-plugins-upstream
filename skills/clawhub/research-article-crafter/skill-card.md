## Description:

Research Article Crafter helps agents plan, research, draft, refine, and review long-form research articles such as technical blogs, industry analyses, white papers, research reports, and deep reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to turn a topic, audience, length, and publishing goal into a sourced long-form article plan and draft. It is intended for research-heavy writing workflows, not short advertising copy, breaking news, literary writing, or formal peer-reviewed publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad command, API-key, and file-processing capabilities for an article-writing workflow.

Mitigation: Review the skill before installation, run it in a limited workspace, and require explicit approval before any command execution or external API call.

Risk: Secrets could be exposed if unnecessary API keys or credentials are provided to the workspace.

Mitigation: Do not provide secrets unless a specific external source is genuinely needed, and keep required API keys in environment variables.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/research-article-crafter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown articles, outlines, research briefs, review notes, title options, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write article drafts to output/{slug}/article.md when used in a workspace.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
