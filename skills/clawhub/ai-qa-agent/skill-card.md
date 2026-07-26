## Description: <br>
AI QA Agent performs structured final QA reviews for code correctness, data integrity, brand voice compliance, and document formatting before a deliverable ships. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mattsteff-hope](https://clawhub.ai/user/mattsteff-hope) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, analysts, and reviewers use this skill as a final quality gate to inspect code, data files, documents, copy, and mixed deliverables. It produces a pass, conditional pass, or fail report with prioritized findings and concrete remediation suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: QA reports can include reviewed content or excerpts and may remain on local disk when saved to the fixed report path. <br>
Mitigation: Use chat-only output or choose a review-specific path for sensitive material, and remove local report files after review when retention is not intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mattsteff-hope/skills/ai-qa-agent) <br>
- [Brand voice guide](artifact/brand-voice-guide.md) <br>
- [Evaluation review artifact](artifact/ai-qa-agent-eval-review.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown QA report with severity-ranked findings, verdict, brand voice scores when applicable, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may instruct the agent to save the report locally at a fixed path; users can request chat-only output or a user-chosen path when reviewing sensitive material.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
