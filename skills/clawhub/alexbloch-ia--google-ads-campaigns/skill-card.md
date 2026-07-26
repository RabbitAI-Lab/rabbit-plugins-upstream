## Description: <br>
Helps agents create reviewable Google Ads search campaign JSON specs, run offline dry-runs, and apply approved campaigns as paused Google Ads objects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and marketing teams use this skill to draft paid search campaign specs, review dry-run plans, and create approved campaigns in a paused state before a human enables them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The mutating path requires Google Ads API credentials for the target account and can create campaign objects. <br>
Mitigation: Use the offline dry-run for review first, run the mutating path only after explicit human approval, and rely on the skill's paused campaign creation before any launch decision. <br>
Risk: The optional budget cap guard can pause every enabled campaign in an account if left unscoped. <br>
Mitigation: Set HARD_CAP and SHEET_URL before scheduling the guard, and strongly consider setting NAME_CONTAINS to limit the guard to intended campaigns. <br>
Risk: Generated ad copy and landing-page choices may be subject to vendor advertising policies and legal constraints. <br>
Mitigation: Have an accountable human review the campaign plan, copy, landing page, targeting, and regulated-vertical requirements before enabling any campaign. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/google-ads-campaigns) <br>
- [Source skill instructions](artifact/SKILL.md) <br>
- [Campaign example JSON](artifact/campaign.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON campaign specs, Python and JavaScript scripts, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Dry-run planning output is intended for human review; mutating use requires Google Ads credentials and creates campaigns paused.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
