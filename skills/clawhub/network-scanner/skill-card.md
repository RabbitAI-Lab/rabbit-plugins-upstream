## Description: <br>
Scan networks to discover devices, gather MAC addresses, vendors, and hostnames. Includes safety checks to prevent accidental scanning of public networks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[florianbeer](https://clawhub.ai/user/florianbeer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, administrators, and security-minded users use this skill to inventory authorized local or private networks, identify devices, and produce network documentation or automation inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network scans can affect systems outside the user's authority if targets or trusted network configuration are wrong. <br>
Mitigation: Use the skill only on networks you own or are authorized to scan, keep blocklists current, and verify CIDR or named network configuration before running scans. <br>
Risk: The current script constructs shell commands from user and configuration input, creating a local command-execution risk. <br>
Mitigation: Avoid untrusted CIDR, DNS, network-name, and config values; prefer --no-sudo unless MAC discovery is required; review the scanner until command execution is changed to validated argument-list subprocess calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/florianbeer/skills/network-scanner) <br>
- [Network Scanner homepage](https://clawhub.com/skills/network-scanner) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown table or JSON network inventory, with shell command examples and JSON configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires nmap and dig; sudo may improve MAC address discovery.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
