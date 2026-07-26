## Description: <br>
Manage and interpret real-time AI agent HTTP/HTTPS traffic monitoring with ClawSec Monitor v3.0, including data exfiltration and injection threat detections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuzhuhai](https://clawhub.ai/user/wuzhuhai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to start, stop, configure, and troubleshoot a local ClawSec Monitor proxy, then interpret AI-agent HTTP/HTTPS traffic detections and threat logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HTTPS interception and threat logs can expose sensitive AI-agent traffic, including secrets or private content. <br>
Mitigation: Install only when local traffic inspection is intended; prefer per-process CA trust or no-MITM mode unless full HTTPS interception is required. <br>
Risk: The local CA and /tmp/clawsec logs may remain on the machine after monitoring. <br>
Mitigation: Protect the generated CA, remove it when finished, and treat /tmp/clawsec logs as sensitive data. <br>


## Reference(s): <br>
- [ClawSec skill page](https://clawhub.ai/wuzhuhai/skills/clawsec) <br>
- [ClawSec Monitor repository](https://github.com/chrisochrisochriso-cmyk/clawsec-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include operational checks, proxy configuration, threat-log interpretation, and troubleshooting steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
