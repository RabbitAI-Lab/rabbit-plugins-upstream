## Description: <br>
Helps agents provide CDN configuration, cache policy, basic security hardening, performance diagnostics, and domain setup guidance for individual developers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and site operators use this skill to draft CDN setup guidance, cache rules, security headers, and diagnostic shell commands for common CDN workflows. It is intended for personal or small-project CDN deployment and optimization tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated provider API or firewall commands could change CDN or host security settings if run automatically. <br>
Mitigation: Review every command before execution, require explicit approval for Cloudflare API and iptables examples, and test changes on non-production systems first. <br>
Risk: API tokens or cloud credentials used with generated commands could have excessive privileges. <br>
Mitigation: Use least-privilege provider tokens and avoid exposing credentials in prompts, logs, or shared command output. <br>
Risk: Firewall allowlist examples can lock out legitimate traffic or omit current provider ranges. <br>
Mitigation: Verify current provider IP ranges, including IPv6 where applicable, and prepare rollback steps before applying firewall rules. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cdn-toolkit-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, Nginx, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include executable CDN provider API, curl, dig, jq, nginx, and firewall command examples that require human review before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
