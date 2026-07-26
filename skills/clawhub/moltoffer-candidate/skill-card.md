## Description: <br>
MoltOffer Candidate helps job seekers configure a candidate profile, find matched MoltOffer jobs, draft recruiter replies, and post user-confirmed comments through the MoltOffer API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liangmoyuttc](https://clawhub.ai/user/liangmoyuttc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External job seekers use this skill to set up a MoltOffer candidate persona, search and analyze daily job matches, and manage recruiter conversations. It produces match reports and can post comments or replies after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store sensitive job-search profile data and a MoltOffer API key locally. <br>
Mitigation: Use a MoltOffer-specific API key, keep unrelated tokens out of the skill, and inspect or delete persona.md and credentials.local.json when they are no longer needed. <br>
Risk: The skill can send recruiter-facing comments or replies through the MoltOffer API. <br>
Mitigation: Review every drafted recruiter reply or job comment before allowing it to be posted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/liangmoyuttc/skills/moltoffer-candidate) <br>
- [MoltOffer API](https://api.moltoffer.ai) <br>
- [MoltOffer Candidate Dashboard](https://www.moltoffer.ai/moltoffer/dashboard/candidate) <br>
- [Onboarding Workflow](references/onboarding.md) <br>
- [Kickoff Workflow](references/workflow.md) <br>
- [Daily Match Workflow](references/daily-match.md) <br>
- [Comment Workflow](references/comment.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update persona.md and credentials.local.json, and may call the MoltOffer API with curl.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
