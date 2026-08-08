## Description: <br>
AI Firewall for Open Claw agents that scrubs inbound messages and tool results for prompt injection, jailbreaks, and data exfiltration attempts using Sentinel's multi-layer detection pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c0ri](https://clawhub.ai/user/c0ri) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to route Open Claw user prompts, tool inputs, tool outputs, and optional LLM proxy traffic through Sentinel for prompt-injection, jailbreak, and data-exfiltration screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts, tool inputs, tool outputs, and optional full LLM proxy traffic to Sentinel's service. <br>
Mitigation: Use it only when Sentinel's retention, logging, and compliance terms are acceptable for the data being processed. <br>
Risk: If the Sentinel key is missing or the service is unreachable, the hook scripts may allow traffic to continue unscanned. <br>
Mitigation: Monitor hook warnings, verify Sentinel connectivity before sensitive sessions, and avoid relying on this skill as the only control for regulated, secret, or proprietary data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/c0ri/skills/sentinel-proxy) <br>
- [Publisher profile](https://clawhub.ai/user/c0ri) <br>
- [Clawdis homepage](https://github.com/c0ri/sentinel-skills) <br>
- [Sentinel AI Firewall](https://sentinelaifirewall.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and hook behavior descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill provides setup instructions and hook scripts that may block, neutralize, flag, or pass scanned content.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
