## Description: <br>
Discover and control Apple media/AirPlay devices (HomePod, Apple TV, AirPlay speakers) from macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[officialpm](https://clawhub.ai/user/officialpm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and macOS users use this skill to discover local Apple media and AirPlay devices, map device names to network identifiers, and issue pairing, playback, routing, and volume commands through pyatv and Airfoil. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill scans the local network and scan output can expose private device names, IP addresses, identifiers, services, and pairing details. <br>
Mitigation: Run scans only on trusted networks, treat scan results as private, and avoid committing or sharing scan output. <br>
Risk: The skill can issue control commands to Apple, AirPlay, and Airfoil-managed devices. <br>
Mitigation: Verify target devices, pyatv, Airfoil, and the neighboring Airfoil skill before granting permissions or issuing control commands. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON scan summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runtime scan output may include local device names, IP addresses, models, identifiers, services, and pairing details.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence and changelog, released 2026-01-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
