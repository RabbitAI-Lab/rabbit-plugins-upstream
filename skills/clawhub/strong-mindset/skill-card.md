## Description: <br>
A Chinese-language conversational coaching skill that reframes user dilemmas through a strong-mindset lens, gives a 24-hour next action, evaluates text, runs a seven-question mindset assessment, generates mindset articles, and refines drafts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[forrestneo](https://clawhub.ai/user/forrestneo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and content creators use this skill for Chinese-language mindset coaching, text assessment, self-reflection quizzes, article generation, and draft refinement. The skill can also produce self-contained HTML reports after an assessment or quiz is completed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may apply a forceful coaching persona too broadly. <br>
Mitigation: Review the style guide before installation and scope use to users who explicitly want direct coaching; require human review for sensitive personal, mental health, employment, or relationship decisions. <br>
Risk: The skill includes persuasive influence and concealed-intent themes. <br>
Mitigation: Use only with explicit consent for coaching or content analysis, avoid deceptive persuasion, and add ethics guardrails for advice involving third parties. <br>
Risk: Assessment and report outputs may look diagnostic even though they are framework-based. <br>
Mitigation: Present scores as reflective coaching outputs, keep the built-in disclaimer, and avoid treating them as clinical or psychometric assessments. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/forrestneo/strong-mindset/tree/main/strong-mindset) <br>
- [ClawHub skill page](https://clawhub.ai/forrestneo/skills/strong-mindset) <br>
- [Strong Mindset style guide](references/style-guide.md) <br>
- [Article corpus README](references/articles/README.md) <br>
- [HTML report generator](references/generate_report.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Chinese-language prose, Markdown reports, JSON report specifications, and self-contained HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Assessment and quiz reports are generated only after substantive user input is evaluated.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
