## Description: <br>
List and snapshot retrieval for webcams, especially foto-webcam.eu, including current JPG snapshot delivery from saved favorites. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unixweb](https://clawhub.ai/user/unixweb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to list configured public webcams, retrieve current snapshots by favorites ID or page URL, and send each selected image through the configured OpenClaw/Telegram channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Favorites entries or direct image URLs may point to untrusted or unintended sources. <br>
Mitigation: Review the favorites list and keep entries limited to public webcam or trusted image URLs before use. <br>
Risk: Snapshot media can be sent to the wrong chat if the Telegram target is misconfigured. <br>
Mitigation: Verify the configured OpenClaw/Telegram target before sending webcam images. <br>


## Reference(s): <br>
- [Photo Webcam on ClawHub](https://clawhub.ai/unixweb/skills/photo-webcam) <br>
- [Publisher profile: unixweb](https://clawhub.ai/user/unixweb) <br>
- [favorites-muenchen.json](artifact/docs/webcams/favorites-muenchen.json) <br>
- [foto-webcam.eu example webcam page](https://www.foto-webcam.eu/webcam/zugspitze/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, configuration] <br>
**Output Format:** [Plain text instructions, JSON script output, shell commands, and JPG snapshot files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maximum 6 webcam images per request; each image is sent with a separate OpenClaw command.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
