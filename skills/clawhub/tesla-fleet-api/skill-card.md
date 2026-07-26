## Description: <br>
Use when integrating with Tesla's official Fleet API to read vehicle and energy device data or issue remote commands such as HVAC preconditioning, vehicle wake, and charge controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and vehicle owners use this skill to configure Tesla Fleet API OAuth access, read vehicle or energy device state, and run approved remote vehicle commands through Tesla's official Fleet API and signed-command proxy flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Tesla account data, vehicle telemetry, location, and remote vehicle controls. <br>
Mitigation: Install only when that access is intended, keep config.json, auth.json, private-key.pem, cached telemetry, and proxy files private, and require explicit approval before unlock, honk, charging, climate, wake, or location commands. <br>
Risk: Signed vehicle commands depend on local proxy and key material that should not be exposed or left running unnecessarily. <br>
Mitigation: Use official Tesla regional URLs or the localhost proxy only, protect proxy files, and stop the proxy when finished. <br>


## Reference(s): <br>
- [Tesla Fleet API ClawHub release](https://clawhub.ai/odrobnik/skills/tesla-fleet-api) <br>
- [SETUP.md](artifact/SETUP.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Tesla virtual key enrollment](https://tesla.com/_ak/YOUR_DOMAIN.com) <br>
- [Tesla Fleet API regional endpoints](https://fleet-api.prd.eu.vn.cloud.tesla.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls] <br>
**Output Format:** [Markdown guidance with CLI commands, Python scripts, JSON configuration, and human-readable or JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and openssl; Tesla client credentials are required, with optional regional, proxy, token, and scope environment variables.] <br>

## Skill Version(s): <br>
1.5.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
