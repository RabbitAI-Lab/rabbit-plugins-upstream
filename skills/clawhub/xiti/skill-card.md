## Description:

Generates heuristic, student-facing competitive-programming explanations that teach problem-solving thinking instead of only presenting final answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Students, educators, and competitive-programming authors use this skill to turn problem statements, URLs, and reference code into explanatory Chinese writeups. It emphasizes intuition, wrong-turn analysis, annotated C++ code, complexity analysis, faithful samples, and iframe-friendly single-file HTML lessons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML lessons can depend on third-party CDN assets for formulas, syntax highlighting, diagrams, and animations.

Mitigation: Review deployment environments for external network access and privacy requirements before publishing or embedding generated HTML.

Risk: Problem URLs, statements, and reference code from untrusted sources may lead to inaccurate or unsafe generated explanations if accepted without review.

Mitigation: Review the generated lesson, code, samples, and any browser-rendered output before sharing it with students or deploying it in a teaching platform.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/xiti)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Chinese instructional prose with annotated C++ code and single-file HTML lesson output when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [HTML outputs may include inline CSS, Mermaid diagrams, KaTeX formulas, highlight.js code highlighting, and anime.js step-through visualizations.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
