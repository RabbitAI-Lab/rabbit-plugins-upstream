## Description: <br>
Bypass API rate limits by rotating VPN servers for OpenVPN-compatible providers such as ProtonVPN, NordVPN, and Mullvad. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[acastellana](https://clawhub.ai/user/acastellana) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use this skill to configure OpenVPN-based IP rotation for high-volume scraping, government APIs, and geo-restricted data workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup grants persistent passwordless sudo for OpenVPN startup and process termination. <br>
Mitigation: Review the sudoers entry before installation, avoid shared or sensitive machines, and remove the sudoers file when the skill is no longer needed. <br>
Risk: VPN credentials are stored in a local plaintext credentials file. <br>
Mitigation: Use dedicated low-privilege VPN credentials, restrict file permissions, and delete ~/.vpn credentials when no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/acastellana/skills/vpn-rotate-skill) <br>
- [ProtonVPN OpenVPN configuration guide](https://protonvpn.com/support/vpn-config-download/) <br>
- [NordVPN OpenVPN configuration downloads](https://nordvpn.com/ovpn/) <br>
- [Mullvad OpenVPN configuration generator](https://mullvad.net/en/account/#/openvpn-config) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Python and bash code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Linux, OpenVPN, VPN provider configuration files, and local VPN credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
