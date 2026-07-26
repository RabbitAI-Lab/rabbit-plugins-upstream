## Description: <br>
WHOOP CLI with health insights, trends analysis, and data fetching for sleep, recovery, HRV, strain, and workouts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koala73](https://clawhub.ai/user/koala73) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to authenticate to WHOOP, fetch personal WHOOP health metrics, and generate summaries, trend views, and wellness-oriented insights from WHOOP API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive WHOOP health and profile data and stores OAuth tokens locally. <br>
Mitigation: Install and run it only in trusted environments, protect WHOOP_CLIENT_SECRET, .env files, and ~/.whoop-cli/tokens.json, and logout or revoke the WHOOP app when access is no longer needed. <br>
Risk: Health insights may be misunderstood as medical advice. <br>
Mitigation: Treat recommendations as general wellness suggestions and rely on qualified professionals for medical decisions. <br>


## Reference(s): <br>
- [WHOOP Developer Portal](https://developer.whoop.com) <br>
- [npm package](https://www.npmjs.com/package/whoopskill) <br>
- [Project homepage](https://github.com/koala73/whoopskill) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Text, Guidance] <br>
**Output Format:** [CLI commands with JSON or human-readable text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 22+ and WHOOP OAuth credentials.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
