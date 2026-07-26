## Description: <br>
Semantic security scanner for OpenClaw skills that detects prompt injection, data exfiltration, and hidden instructions that traditional code scanners miss. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fermionoid](https://clawhub.ai/user/fermionoid) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security reviewers use Senseguard to scan OpenClaw skills for natural-language security threats such as prompt injection, data exfiltration, obfuscation, and persistence instructions before installation or release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Semantic results can be overstated when Layer 2 LLM analysis has not actually been performed or integrated. <br>
Mitigation: Manually process any generated layer2_prompt and integrate the returned JSON before relying on a SAFE semantic result. <br>
Risk: Cached scan results may persist information about private skill targets in the default local cache. <br>
Mitigation: Use narrow scan targets and a controlled --cache-file, or run with --no-cache for sensitive private skills. <br>
Risk: Automated scanner output can be incomplete or misleading if treated as a final security decision. <br>
Mitigation: Use Senseguard as local triage and review results manually before relying on them for deployment or installation decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fermionoid/skills/senseguard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown risk report or JSON scan results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include a score, rating, findings, evidence text, line numbers, and recommendations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
