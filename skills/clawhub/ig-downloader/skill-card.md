## Description: <br>
Download Instagram profile media, including reels, photos, and carousel images, using a sessionid cookie, an interactive Playwright setup flow, or an Apify dataset fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cripterhack](https://clawhub.ai/user/cripterhack) <br>

### License/Terms of Use: <br>
GPL-2.0-only <br>


## Use Case: <br>
Developers and agent users use this skill to choose the correct command-line mode for downloading Instagram profile posts and reels into local media files. It is most relevant when the user can provide or create an Instagram sessionid, or when an Apify dataset is available as a fallback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses and may store an Instagram sessionid, which should be treated like an account credential. <br>
Mitigation: Use the setup or sessionid flow only for accounts you control, avoid pasting sessionid values into shared logs or shell history, and revoke or refresh the Instagram session if exposure is suspected. <br>
Risk: The setup and fallback flows can access browser cookies or ask the user to paste session data. <br>
Mitigation: Review the local script before installation, prefer manual or local installation over one-line remote installers, and confirm where the config file is stored before running setup. <br>
Risk: The downloader depends on external Instagram and Apify behavior, including session expiry, private profile access, and expiring CDN URLs. <br>
Mitigation: Expect runs to fail when sessions expire or remote data changes, re-run setup for expired sessions, and download Apify-sourced media soon after collecting the dataset. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cripterhack/skills/ig-downloader) <br>
- [Repository](https://github.com/cripterhack/ig-downloader-skill) <br>
- [Issues](https://github.com/cripterhack/ig-downloader-skill/issues) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with command-line examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance selects between sessionid, setup, and Apify fallback modes and describes local media file outputs.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
