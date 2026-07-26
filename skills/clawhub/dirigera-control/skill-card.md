## Description: <br>
Controls IKEA Dirigera smart home devices through a hub, including lights, outlets, scenes, controllers, status checks, hub discovery, and token setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[falderebet](https://clawhub.ai/user/falderebet) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and home automation operators use this skill to let an agent inspect and control IKEA Dirigera smart home devices, generate hub access tokens, find the hub on a local network, and produce status or battery reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated Dirigera hub control token can be saved to a local text file. <br>
Mitigation: Treat the token as a secret, store it only in a private location, and delete it after use when persistent access is not required. <br>
Risk: The skill can perform broad live device actions, including whole-home light or outlet shutdown. <br>
Mitigation: Require explicit user confirmation before whole-home, outlet, scene, or other broad control actions. <br>
Risk: Hub access through a tunnel or VPS could expose smart-home control outside the local network. <br>
Mitigation: Avoid exposing the hub through a tunnel unless access is fully controlled and intended. <br>
Risk: Hub discovery can probe local subnet candidates on the Dirigera port. <br>
Mitigation: Run discovery only on networks the user owns or administers, and scope subnet scans narrowly. <br>


## Reference(s): <br>
- [Dirigera API Complete Reference](artifact/references/api.md) <br>
- [Common Usage Patterns](artifact/references/patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python and bash code blocks, plus plain text status messages and JSON-like status dictionaries from helper functions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run local network probes and live Dirigera API calls when the user supplies hub access details and completes physical pairing.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
