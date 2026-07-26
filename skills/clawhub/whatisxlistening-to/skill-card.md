## Description: <br>
Query Last.fm listening data, show now playing, sync scrobble history to local DB, and deploy a personal "now playing" web dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[poiley](https://clawhub.ai/user/poiley) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and personal automation agents use this skill to answer Last.fm now-playing, listening-stat, and scrobble-history questions. Developers can also use it to configure and deploy a personal Last.fm dashboard backed by local SQLite sync. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release bundle includes unrelated workspace materials and high-privilege automation instructions. <br>
Mitigation: Audit the entire bundle before installing, and prefer a republished package containing only the Last.fm dashboard skill files. <br>
Risk: The security evidence reports plaintext remote-access credentials in bundled workspace materials. <br>
Mitigation: Do not reuse exposed values; rotate any affected credentials before deployment or redistribution. <br>
Risk: Backfilling listening history and exposing a dashboard can reveal personal music activity patterns. <br>
Mitigation: Document the backfill scope, keep API keys in secrets, and restrict dashboard exposure when the listening history should remain private. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/poiley/skills/whatisxlistening-to) <br>
- [Publisher profile](https://clawhub.ai/user/poiley) <br>
- [Live demo](https://whatisbenlistening.to) <br>
- [Last.fm API account setup](https://www.last.fm/api/account/create) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local Last.fm CLI commands, JSON configuration examples, Kubernetes deployment guidance, and dashboard/API usage guidance.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata; artifact pyproject.toml reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
