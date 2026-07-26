## Description: <br>
Review Diagnostics is a manuscript review toolkit that helps agents apply fact-checking, reader simulation, structure analysis, communicative impact assessment, and AI-authenticity checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and content-review agents use this skill to diagnose articles, podcast drafts, and video scripts before publication. It guides review work across factual accuracy, reader reaction, structure, style drift, and AI-like writing patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional helper scripts can create checklist files and inspect local review/source directories when run. <br>
Mitigation: Use the scripts only in projects where the docs/reviews/<article-name> convention is acceptable, and review generated or validated artifacts before relying on them. <br>


## Reference(s): <br>
- [Fact-check review guidance](references/fact-check.md) <br>
- [Reader simulation guidance](references/reader-sim.md) <br>
- [Structural review guidance](references/structural-review.md) <br>
- [Review techniques catalog](references/techniques.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown review findings, JSON checklist files, and terminal validation output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Helper scripts create checklist files and inspect local review/source directories only when explicitly run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
