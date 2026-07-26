## Description: <br>
Scan OpenClaw/Hermes skills for risky permission patterns before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect third-party OpenClaw or Hermes skill folders before installation and to audit their own skills before publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes a CI verifier that can execute Python code from scanned skill folders. <br>
Mitigation: Run ci/verify_product.py only in a hardened sandbox with no secrets and limited filesystem and network access. <br>
Risk: The security verdict is suspicious because the CI verifier behavior is under-disclosed. <br>
Mitigation: Install only when you intend to use the documented local agent_sentinel.py scan command and review bundled CI files before use. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/itspremkumar/skills/agent-sentinel) <br>
- [Publisher profile](https://clawhub.ai/user/itspremkumar) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON risk report with command-line status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports scanned file count, risk level, approval-gate status, shell hits, secret hits, and findings.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
