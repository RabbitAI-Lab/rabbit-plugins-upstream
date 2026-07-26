## Description: <br>
Live game odds and fixtures via propzapi.com, with tools for moneyline, spreads, totals, fixtures, live scores, and covered sportsbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paperandbeyond23-gif](https://clawhub.ai/user/paperandbeyond23-gif) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they need live sports odds, schedules, scores, or covered sportsbook data from Propzapi. It is intended for informational odds lookups, not wagering, betting advice, player props, or season statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Propzapi API key and sends it to Propzapi for live API requests. <br>
Mitigation: Install only if you are comfortable providing PROPZAPI_KEY to this skill, and store the key using your normal secret-management practices. <br>
Risk: Live odds, schedules, scores, and sportsbook lookups may consume Propzapi credits. <br>
Mitigation: Use the skill only for explicit live odds or fixture requests and monitor Propzapi credit usage. <br>
Risk: The documentation warns against using this skill for player props, betting picks, season stats, or wagering decisions. <br>
Mitigation: Route player-prop requests to an appropriate Propzapi skill and treat returned odds as informational, potentially delayed data rather than betting advice. <br>


## Reference(s): <br>
- [Propzapi homepage](https://propzapi.com) <br>
- [Propzapi app and API keys](https://propzapi.com/app) <br>
- [Propzapi pricing](https://propzapi.com/pricing) <br>
- [ClawHub skill page](https://clawhub.ai/paperandbeyond23-gif/skills/propzapi-odds) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON-like dictionaries returned to the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PROPZAPI_KEY and may spend Propzapi credits when live odds, events, or sportsbook data are requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
