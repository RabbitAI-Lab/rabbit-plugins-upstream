## Description: <br>
Monitor Bitaxe Gamma Bitcoin miner status via HTTP API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pietro395](https://clawhub.ai/user/pietro395) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to check the status, hashrate, temperature, power consumption, and statistics of a Bitaxe Gamma or compatible Bitcoin miner through its HTTP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The script contacts the HTTP address configured by the user. <br>
Mitigation: Use only an IP address for a Bitaxe device you control, preferably on your local network. <br>
Risk: The script can save the miner IP locally in ~/.config/bitaxe-monitor/config.json. <br>
Mitigation: Review or remove the config file if the saved miner address should no longer be used. <br>
Risk: The skill is published by a third-party ClawHub user. <br>
Mitigation: Review the script and scanner guidance before running it in an environment with sensitive network access. <br>


## Reference(s): <br>
- [Bitaxe Monitor on ClawHub](https://clawhub.ai/pietro395/skills/bitaxe-monitor) <br>
- [Bitaxe API documentation](https://osmu.wiki/bitaxe/api/) <br>
- [ESP-Miner OpenAPI specification](https://github.com/bitaxeorg/ESP-Miner/blob/master/main/http_server/openapi.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands, plus text or JSON status output from the script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script reads a miner IP from an argument, config file, or BITAXE_IP and can save the IP to ~/.config/bitaxe-monitor/config.json.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
