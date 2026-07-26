## Description: <br>
Brief turns user-provided source material into decision-ready executive summaries, status updates, meeting pre-reads, handoffs, incident updates, and decision documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and teams use Brief to transform user-provided documents, threads, transcripts, metrics, or verbal context into action-oriented briefs for executives, stakeholders, meetings, incidents, handoffs, and decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local preference and configuration files may retain briefing style preferences or free-form feedback. <br>
Mitigation: Avoid putting sensitive free-form information into preference feedback, and review or delete ~/Clawic/data/brief/ to reset what the skill has learned. <br>
Risk: Briefs can mislead if source material is stale, incomplete, conflicting, or missing clear provenance. <br>
Mitigation: Use user-provided sources, include source and as-of dates, show conflicts and gaps, and review the brief before acting on it. <br>
Risk: Locale and timezone defaults can affect how dates, currencies, and timestamps are presented. <br>
Mitigation: Review Clawic profile defaults and the Brief config file when the brief must match a specific audience or region. <br>


## Reference(s): <br>
- [Brief on ClawHub](https://clawhub.ai/ivangdavila/skills/brief) <br>
- [Brief homepage](https://clawic.com/skills/brief) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown briefs with structured sections, bullets, status labels, explicit asks, source lines, and optional local preference files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local configuration and learned preference files under ~/Clawic/data/brief/ when the user states or signals preferences.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
