## Description: <br>
Generate QR code for Wi-Fi credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and end users use this skill to generate a Wi-Fi QR code from an SSID, password, and optional security type so devices can join a network without manually typing the password. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wi-Fi passwords can appear in command examples, generated QR codes, saved images, screenshots, or terminal history. <br>
Mitigation: Treat these outputs as sensitive, prefer guest networks when possible, and delete or protect generated QR outputs after use. <br>
Risk: The skill depends on the qrencode command-line tool being available on the host system. <br>
Mitigation: Install qrencode from a trusted package manager before using generated commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/wifi-qr) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands depend on qrencode being installed and may include sensitive Wi-Fi credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
