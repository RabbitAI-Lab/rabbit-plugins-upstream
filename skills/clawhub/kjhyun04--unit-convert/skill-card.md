## Description: <br>
Converts length, mass, volume, area, speed, temperature, and digital storage units offline using a bundled conversion table. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kjhyun04](https://clawhub.ai/user/kjhyun04) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and end users use this skill to convert supported units without guessing or calling an external API. It is suited for everyday Korean and English unit-conversion questions where the answer should come from the bundled table. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversion accuracy is limited to the included units and factors. <br>
Mitigation: Check supported units with --list and avoid assuming conversions outside the bundled table. <br>
Risk: Unsupported units or cross-dimension requests can produce incorrect answers if an agent guesses a substitute conversion. <br>
Mitigation: Use the script error as authoritative, explain the limitation, and do not substitute units or density assumptions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kjhyun04/skills/unit-convert) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text conversion results or JSON from the bundled command-line script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and uses only the bundled unit table; no network, credentials, persistence, or broad system access are requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
