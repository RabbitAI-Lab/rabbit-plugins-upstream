## Description:

AI citability scoring and optimization. Analyzes web page content to determine how likely AI systems (ChatGPT, Claude, Perplexity, Gemini) are to cite or quote passages from the page. Provides a citability score (0-100) with specific rewrite suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to analyze web pages for AI citability and receive a scored markdown report with rewrite suggestions for improving extractable, quotable passages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches user-provided URLs and writes an analysis markdown file in the workspace.

Mitigation: Use it only with URLs and workspaces the user is comfortable analyzing, and review the generated markdown before relying on recommendations.

Risk: The skill has Bash permission for documented citability tooling.

Mitigation: Limit Bash use to the documented seogeo citability and block analysis commands, not unrelated shell activity.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with citability scores, tables, quoted passage excerpts, and rewrite recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces GEO-CITABILITY-SCORE.md in the workspace and may use URL fetching or local HTML analysis depending on the input.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
