## Description: <br>
Connects to and controls the Acasis Flow HID dock on Windows, including connection checks, view switching, report reads, and explicitly requested raw HID payload sends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[facaihero](https://clawhub.ai/user/facaihero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users with an Acasis Flow HID dock use this skill on Windows to install or invoke the hid-dock CLI, check device connection, switch dock views, list or read HID reports, and send intentionally provided raw HID payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads and runs an unverified Windows executable from a GitHub release on first use. <br>
Mitigation: Install only when the publisher and release source are trusted; verify provenance or hashes when available and confirm the executable path under .openclaw tools before running it. <br>
Risk: The raw send command can transmit arbitrary HID payload bytes to the connected dock. <br>
Mitigation: Use the documented info, list, read, and view commands for normal workflows; send raw payloads only when the user intentionally provides exact bytes for the Acasis Flow dock. <br>
Risk: The skill is limited to Windows and to the Acasis Flow HID dock, and device access can fail when another app holds the HID device open. <br>
Mitigation: Run it only on Windows with the target dock connected and powered; close other dock-control software before retrying failed connection or view commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/facaihero/skills/hid-dock) <br>
- [hid-dock Windows x64 release asset](https://github.com/facaiHero/hid-dock/releases/download/v1.0.0/hid-dock-win-x64.zip) <br>
- [Publisher profile](https://clawhub.ai/user/facaihero) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown guidance with PowerShell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Windows-only workflow for a fixed Acasis Flow HID device VID/PID and 64-byte HID reports.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
