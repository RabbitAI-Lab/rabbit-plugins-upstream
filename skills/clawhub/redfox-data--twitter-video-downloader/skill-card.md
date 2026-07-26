## Description: <br>
X(Twitter) Video Downloader parses a single X or Twitter video tweet link through the redfox.hk API and returns a watermark-free direct video download URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, editors, collectors, operators, and researchers use this skill to turn a public X/Twitter video post URL into a direct download link for saving, editing, backup, or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted X/Twitter links and the RedFox API key are sent to redfox.hk for processing. <br>
Mitigation: Use only public, non-sensitive links when comfortable with RedFox handling that data, and keep the key in REDFOX_API_KEY instead of prompts, logs, or shared files. <br>
Risk: Passing an API key on the command line or saving it locally can expose credentials through shell history, process inspection, or local file access. <br>
Mitigation: Prefer the environment variable workflow, avoid command-line key entry, and rotate or revoke the key if it may have been exposed. <br>
Risk: Private, deleted, or unavailable posts may fail to parse or return incomplete results. <br>
Mitigation: Use complete public x.com or twitter.com status URLs and handle parser failures before relying on the returned download link. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/twitter-video-downloader) <br>
- [RedFox API key page](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [redfox.hk X video download API endpoint](https://redfox.hk/story/api/parseWork/videoDownload/x) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Terminal text or JSON containing video description, resource metadata, download URLs, and cover URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires one public X/Twitter video URL and a REDFOX_API_KEY; optional JSON output is available with the script flag.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
