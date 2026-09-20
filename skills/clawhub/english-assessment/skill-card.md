## Description: <br>
English Assessment is a companion-style English proficiency assessment agent that generates adaptive CEFR B1-C2 question sets, silently scores answers, tracks weak areas, and supports wrong-answer review, progress analysis, and data import/export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[z-zihan](https://clawhub.ai/user/z-zihan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Learners use this skill to take adaptive English level assessments, receive score reports and weak-area analysis, review wrong answers, and track learning progress over repeated sessions. It is not positioned as a full English course, general translation tool, or open-ended English chat assistant. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores English assessment history, wrong-answer data, tested knowledge points, and recent question data locally. <br>
Mitigation: Install only if local persistence is acceptable, and review or delete the ./english-assessment data files when retention is no longer needed. <br>
Risk: The skill uses web search and fetch behavior for question sourcing and includes a hidden DIAG-SEARCH network diagnostic section. <br>
Mitigation: Review or remove the DIAG-SEARCH section before installation, and allow network access only when web-sourced questions are intended. <br>
Risk: The skill can sync exported assessment data to Feishu cloud documents when document permissions are available. <br>
Mitigation: Prefer local-only export unless cloud backup is intentional, and verify Feishu document access permissions before syncing or importing data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/z-zihan/english-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Feishu-compatible Markdown-style chat messages and JSON data exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local JSON files for wrong answers, assessment history, tested knowledge points, current tests, recent questions, and exports.] <br>

## Skill Version(s): <br>
4.15.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
