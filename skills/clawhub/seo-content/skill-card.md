## Description:

Content quality and E-E-A-T analysis with AI citation readiness assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, and SEO practitioners use this skill to audit pages or drafts for content quality, E-E-A-T signals, readability, thin-content issues, and AI citation readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to fetch public pages or inspect user-provided drafts for SEO analysis.

Mitigation: Use it only with URLs or content that can be shared with the agent and any optional analysis tools.

Risk: Optional DataForSEO or seogeo tooling may receive URLs, keywords, or content inputs.

Mitigation: Enable optional tooling only when the user is comfortable sending those inputs to the relevant tool provider.

Risk: SEO quality and AI citation scores are heuristic and can be mistaken for guaranteed ranking outcomes.

Mitigation: Present scores as advisory, validate findings against official search guidance, and avoid promising ranking improvements.

## Reference(s):

- [Google Search Central: Creating Helpful, Reliable, People-First Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with scores, E-E-A-T breakdown, issues, recommendations, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use optional DataForSEO or seogeo tooling when available; reports should state that heuristic scores are not Google-internal ranking signals.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
