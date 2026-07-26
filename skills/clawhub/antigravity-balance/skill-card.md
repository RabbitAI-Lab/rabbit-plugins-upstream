## Description: <br>
Check Google Antigravity AI model quota/token balance by detecting the local Antigravity language server process and querying its local API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[finderstrategy-cyber](https://clawhub.ai/user/finderstrategy-cyber) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Antigravity users use this skill to check quota status, remaining model token balance, and reset timing from a running local Antigravity or Windsurf instance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Terminal or JSON output can expose account identity, tier, quota status, and reset timing. <br>
Mitigation: Avoid shared terminals, screen recordings, logs, and saved JSON output when account or quota details should remain private. <br>
Risk: The script reads local Antigravity process arguments and uses a local CSRF token to query the local Antigravity API. <br>
Mitigation: Run the skill only in a trusted local session after reviewing the artifact, and avoid verbose mode where token-bearing process data could be exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/finderstrategy-cyber/skills/antigravity-balance) <br>
- [Publisher Profile](https://clawhub.ai/user/finderstrategy-cyber) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Terminal text or JSON output, with Markdown guidance and shell commands when used by an agent.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes account identity and quota details; treat output as sensitive.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
