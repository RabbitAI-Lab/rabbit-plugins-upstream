## Description: <br>
Agent Touch Layer helps agents automate browser and native iOS Simulator workflows through local ATL HTTP commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jordancoin](https://clawhub.ai/user/jordancoin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to drive iPhone and iPad Simulator browser and native app tasks, including navigation, UI inspection, screenshots, touch gestures, JavaScript evaluation, app launch, and form entry. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release builds and installs an iOS Simulator app from a mutable external GitHub branch. <br>
Mitigation: Install only after reviewing the referenced repository and pinning or auditing the code used for the build. <br>
Risk: The skill exposes powerful browser and native app automation, including screenshots, accessibility snapshots, JavaScript evaluation, form entry, and cookie operations. <br>
Mitigation: Use isolated simulator profiles and test accounts, and avoid sensitive apps or logged-in sites unless the session-level access is intentional. <br>
Risk: Security evidence marks the release suspicious because it combines mutable external code with sensitive automation capabilities. <br>
Mitigation: Treat the skill as requiring careful local review before installation and restrict use to trusted workflows. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/jordancoin/skills/atl-mobile) <br>
- [Publisher profile](https://clawhub.ai/user/jordancoin) <br>
- [ATL install repository](https://github.com/JordanCoin/Atl) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target local ATL HTTP servers and may produce JSON responses, screenshots, PDFs, accessibility snapshots, DOM data, and cookie data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
