## Description: <br>
Download YouTube videos and upload them to Pocket Casts Files for offline viewing. For personal use with content you own or have rights to. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manuelhettich](https://clawhub.ai/user/manuelhettich) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to download YouTube videos they own or have rights to and upload MP4 files to Pocket Casts Files for offline viewing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow stores a Pocket Casts refresh token and YouTube cookies on the local machine. <br>
Mitigation: Keep credentials in a private credentials directory with restrictive file permissions and treat both files like passwords. <br>
Risk: Troubleshooting output or failed-run logs may expose sensitive account data. <br>
Mitigation: Review logs for secrets before sharing them and rotate affected tokens or cookies if they are exposed. <br>
Risk: The setup notes include installing Deno through a remote shell installer. <br>
Mitigation: Prefer a trusted package manager or inspect the installer before running it. <br>
Risk: Downloading or uploading media without sufficient rights can violate service terms or copyright law. <br>
Mitigation: Use the skill only for personal recordings, Creative Commons media, creator-permitted downloads, or other content you own or have rights to. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/manuelhettich/skills/pocket-casts-yt) <br>
- [Pocket Casts](https://pocketcasts.com) <br>
- [Deno install script](https://deno.land/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with shell commands and terminal status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local Pocket Casts refresh token and optional YouTube cookies; uploads MP4 files through Pocket Casts.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
