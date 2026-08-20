## Description:

Provides guidance and shell scripts for running MetaTrader 5 headlessly on Linux/VPS with Wine, Xvfb, xdotool, OCR-guided EA attachment, deployment, heartbeat monitoring, and automatic restart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, operators, and traders use this skill to configure and manage headless MetaTrader 5 Expert Advisor workflows on Linux/VPS systems. It helps automate EA attachment, deployment verification, heartbeat checks, and MT5 restarts for 24/7 trading operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scripts can restart MT5 and reattach Expert Advisors on a trading machine, which could disrupt or resume live trading unexpectedly.

Mitigation: Test on a demo account first and review restart, heartbeat, and EA attachment behavior before using the scripts with live funds.

Risk: Broad shell and process-control commands may affect the wrong MT5 or Wine process if used on a shared host.

Mitigation: Run the workflow in a dedicated Wine/MT5 profile or isolated VPS account and narrow process matching before production use.

Risk: Broker-login workflows can expose sensitive account access if credentials are stored in scripts, shell history, or shared environments.

Mitigation: Keep broker passwords out of scripts and shell history, restrict host access, and use broker-side account protections where available.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell script examples and executable bash scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational instructions and scripts that control local MT5, Wine, Xvfb, OCR, and process restart workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
