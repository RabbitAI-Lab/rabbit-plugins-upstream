## Description: <br>
Provides a weekly diagnostic report for an AlphaGBM research knowledge base, flagging stale profiles, thesis drift, orphan pages, and prioritized recommendations with an overall 0-100 health score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External AlphaGBM users and agents use this skill to inspect the state of a research workspace, retrieve or generate a health report, and decide which stale profiles, drifted theses, or orphan pages need attention. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can surface archive or delete recommendations for research profiles. <br>
Mitigation: Treat health reports as read-only unless the user explicitly requests a follow-up action, and require a separate confirmation with the exact ticker before any archive or delete action. <br>
Risk: The skill uses ALPHAGBM_API_KEY to access a user's AlphaGBM research workspace. <br>
Mitigation: Install only for the intended AlphaGBM workspace, keep the API key in the environment, and avoid exposing more report detail than needed for the user's request. <br>
Risk: Health scores, stale-profile flags, and thesis-drift findings may be incomplete or outdated. <br>
Mitigation: Show the report date and recommendation reasons, and ask the user to review proposed refresh, thesis review, archive, or thesis creation actions before applying related skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-health-check) <br>
- [AlphaGBM website](https://alphagbm.com) <br>
- [AlphaGBM API base URL](https://alphagbm.zeabur.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown summaries with API request and JSON response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ALPHAGBM_API_KEY; on-demand report generation is Pro-only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
