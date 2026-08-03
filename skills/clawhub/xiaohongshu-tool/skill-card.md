## Description: <br>
Helps agents query public Xiaohongshu notes, note details, comments, and creator posts for content research, competitor analysis, KOL screening, and trend insight. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[um-why](https://clawhub.ai/user/um-why) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, brand marketers, market analysts, and operations teams use this skill to collect public Xiaohongshu research data for topic discovery, competitor monitoring, comment analysis, creator tracking, and report preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Xiaohongshu keywords or URLs and the GUAIKEI_API_TOKEN are sent to the guaikei.com API service. <br>
Mitigation: Use the skill only when third-party API processing is acceptable, scope tokens appropriately, and avoid submitting sensitive research targets. <br>
Risk: Generated logs can retain competitive research data on the local machine. <br>
Mitigation: Run on managed devices for sensitive work and review, secure, or delete logs according to the user's data-retention needs. <br>


## Reference(s): <br>
- [Guaikei Xiaohongshu API service](https://www.guaikei.com) <br>
- [Complete options reference](references/options.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved locally under logs for later analysis.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata, SKILL.md metadata, package.json, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
