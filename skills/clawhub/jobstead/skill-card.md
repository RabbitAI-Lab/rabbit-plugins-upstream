## Description:

Helps a job-seeker decide whether a role is actually worth their time, then tells their story for it beautifully.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adibas03](https://clawhub.ai/user/adibas03)

### License/Terms of Use:

MIT-0

## Use Case:

External job seekers use Jobstead to assess role fit, identify likely scam postings, tailor truthful resumes and cover letters, and continue a multi-session job search using profile, tracker, lesson, and log state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses persistent job-search state that can include personal profile details and application history.

Mitigation: Run it in a dedicated workspace or account and review any state it says it found before relying on it.

Risk: The security review notes broad persistent memory discovery and quiet lesson capture as areas needing review before use.

Mitigation: Restrict state recovery and lesson storage to an explicit Jobstead path or namespace, and require approval before using external memory or saving new reusable lessons.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/adibas03/jobstead/tree/master/skills/jobstead)
- [ClawHub skill page](https://clawhub.ai/adibas03/skills/jobstead)
- [Jobstead playbook](https://raw.githubusercontent.com/adibas03/jobstead/refs/tags/v3.6/Jobstead.md)
- [Applicant profile reference](references/profile.md)
- [Application tracker reference](references/tracker.md)
- [Lessons reference](references/lessons.md)
- [Session log reference](references/log.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text with role-fit analysis, scam checks, recommendations, and tailored resume or cover-letter content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose updates to persistent profile, tracker, lessons, and session log files for the user's confirmation.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
