## Description: <br>
Clawsec Feed helps agents monitor OpenClaw-related security advisories, check advisory-feed data, and alert users about affected installed skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent users use this skill to install or consult an advisory feed, fetch current security advisory JSON, and compare advisories against locally installed skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes shell snippets for downloading release metadata, artifacts, and advisory-feed data. <br>
Mitigation: Review shell snippets before execution and verify release source, signatures, and checksums before installing on production hosts. <br>
Risk: The skill may read locally installed skill names to cross-reference advisories. <br>
Mitigation: Run checks in the intended skill directory only and avoid exposing unrelated local paths or private package names. <br>
Risk: The advisory feed and release metadata are network-fetched and can become unavailable or stale. <br>
Mitigation: Handle fetch failures explicitly and confirm critical findings against the published advisory details before taking action. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/clawsec-feed) <br>
- [ClawSec Advisory Feed](https://raw.githubusercontent.com/prompt-security/ClawSec/main/advisories/feed.json) <br>
- [ClawSec Release Artifacts](https://github.com/prompt-security/ClawSec/releases) <br>
- [Prompt Security](https://prompt.security) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May fetch advisory-feed JSON and compare advisories with locally installed skill names when the agent follows the guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
