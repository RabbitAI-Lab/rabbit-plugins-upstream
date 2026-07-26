## Description: <br>
Cast YouTube videos, Tubi TV show episodes, and TV show episodes from other video streaming apps via ADB to Chromecast with Android TV. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antgly](https://clawhub.ai/user/antgly) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to pair with a Chromecast with Google TV, check device status, start YouTube or Tubi playback, route other episodic content through Google TV search, and send media pause or resume commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ADB wireless debugging and pairing can give the host control over the paired Chromecast device. <br>
Mitigation: Use the skill only on a trusted network with an intended device, pass explicit device details, and disable debugging or remove old ADB pairings when finished. <br>
Risk: Weak input validation can expose a paired TV to unsafe ADB shell command behavior through untrusted URLs or arbitrary search strings. <br>
Mitigation: Use trusted Tubi URLs and search strings, review requested playback actions before execution, and avoid passing untrusted input to the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/antgly/skills/chromecast-with-google-tv) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [yt-api CLI](https://github.com/nerveband/youtube-api-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke local ADB, scrcpy, uv, and yt-api tooling and may update a local Chromecast device cache.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and changelog, released 2026-02-12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
