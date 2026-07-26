## Description: <br>
XSkill ARE evaluates AI skills across business value, prompt quality, robustness, safety, composability, and cost, producing structured reliability scores and reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reviewers, and skill publishers use XSkill ARE to assess an AI skill's release quality and reliability before adoption. It supports rubric-driven scoring, red-team-style robustness and safety checks, calibration review, and fatal-flaw reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LLM-judge scores can be affected by judge subjectivity, model drift, calibration limits, and language coverage gaps. <br>
Mitigation: Treat scores as advisory, review high-impact results manually, and check calibration status and judge consensus before relying on the assessment. <br>
Risk: The skill uses adversarial test prompts and disclosed rubrics to assess other skills, which can produce harsh or incomplete conclusions if inputs are sparse or outside covered scenarios. <br>
Mitigation: Provide complete skill content and capabilities, review fatal-flaw findings against the original skill behavior, and supplement with domain-specific tests where needed. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/qomob/xskill-are) <br>
- [ClawHub skill page](https://clawhub.ai/qomob/skills/xskill-are) <br>
- [Output schema](references/output-schema.md) <br>
- [Scoring formulas](references/scoring-formulas.md) <br>
- [Business value rubric](references/rubric-business.md) <br>
- [Safety rubric](references/rubric-safety.md) <br>
- [Robustness rubric](references/rubric-robustness.md) <br>
- [Multi-judge protocol](references/multi-judge-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Structured AIScore and AIReport objects with concise explanatory report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scores cover six dimensions, HRR tiering, calibration status, judge consensus, fatal flaws, strengths, weaknesses, and test case results.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence; artifact frontmatter reports evaluator version 2.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
