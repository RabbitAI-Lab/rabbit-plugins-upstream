## Description:

Meta Deep Research helps agents run structured deep research through outline creation, parallel search, report synthesis, self-verification, reflection, and reusable learning notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research-focused agents use this skill to break a research topic into an outline and fields, gather structured evidence through web search, and synthesize a traceable Markdown report. It is suited to literature reviews, benchmark comparisons, technical evaluations, market research, and due diligence where source-backed findings and uncertainty notes are important.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research outputs and local learning history may capture sensitive topics, user preferences, notes, or personal data.

Mitigation: Keep research outputs in a dedicated folder, avoid entering secrets or sensitive personal data in notes or preferences, and delete learned_patterns.json when cross-session learning should not persist.

Risk: Generated research can be incomplete or misleading when search access is unavailable, sources are sparse, or the distilled workflow misses implicit behavior from the teacher skill.

Mitigation: Review cited sources and uncertainty notes before relying on findings, and verify key decisions against primary evidence or the original teacher workflow when stakes are high.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-deep-research)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Files, Guidance]

**Output Format:** [Markdown report plus outline.yaml, fields.yaml, structured result files, and local learning JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research outputs include source and uncertainty notes; the learner can update learned_patterns.json with usage history, preferences, and reflection data.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
