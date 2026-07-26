## Description: <br>
Provides real-time Old School RuneScape player statistics, leaderboard data, game-mode filters, and player comparison through an MCP-backed API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to retrieve and compare Old School RuneScape player stats, skill leaderboards, and activity leaderboards through the XiaoBenYang MCP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and saves it in a plaintext .env file in the working directory. <br>
Mitigation: Use a limited and revocable API key, avoid sensitive repositories, and remove the .env file when the skill is no longer needed. <br>
Risk: Mismatched GaoKao/XiaoBenYang project references make the exact scope less clear. <br>
Mitigation: Review the artifact text and scripts before routine use, and correct stale references before relying on the skill operationally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/osrs-stat) <br>
- [XiaoBenYang API key and service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration guidance] <br>
**Output Format:** [JSON API responses summarized as text or Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key before live data can be retrieved.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
