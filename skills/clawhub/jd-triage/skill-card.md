## Description: <br>
Scores job descriptions on desirability and candidacy against a user's criteria and skills, then returns one concrete action. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bwancoding](https://clawhub.ai/user/bwancoding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers use this skill to evaluate a pasted job description or recruiter message against their saved career criteria, skills, and history. It also supports criteria setup, evaluation history review, role comparison, trend analysis, and skill-gap planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores local Markdown files containing career preferences, compensation floors, locations, skills, and job-evaluation summaries. <br>
Mitigation: Keep the workspace private, and avoid enabling full raw JD history in a synced or shared workspace unless storing recruiter details or non-public compensation text there is acceptable. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [Bootstrap](artifact/references/bootstrap.md) <br>
- [Scoring](artifact/references/scoring.md) <br>
- [History](artifact/references/history.md) <br>
- [Analyze and Plan](artifact/references/analysis-commands.md) <br>
- [Intensity Signals](artifact/references/intensity-signals.md) <br>
- [ClawHub skill page](https://clawhub.ai/bwancoding/skills/jd-triage) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Conversational Markdown plus local Markdown criteria and history files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update jd_criteria.md and jd_history.md under ~/.openclaw/workspace.] <br>

## Skill Version(s): <br>
1.1.1 (source: release metadata and skill heading) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
