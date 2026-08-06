## Description: <br>
This skill helps agents run yt-mem-ai YouTube pipeline operations, including video ingestion, subscription discovery, batch fetching, library search, ratings, recommendations, compilations, supercuts, status checks, and daily or single-video workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dasein108](https://clawhub.ai/user/dasein108) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to operate a YouTube memory pipeline through yt-mem-ai CLI commands. It guides agents through ingesting videos, querying stored transcripts, managing configuration, creating compilations or supercuts, and delegating analysis outputs to yt-agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to persistently enable browser-cookie access for YouTube fetches. <br>
Mitigation: Use a dedicated browser profile or account where possible, confirm the session should be used, and unset the browser-cookie setting when it is no longer needed. <br>
Risk: The external yt-mem-ai CLI stores YouTube-related configuration globally. <br>
Mitigation: Install only when global configuration storage is acceptable, inspect settings with the CLI before use, and remove sensitive or unneeded settings after the workflow. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and optional JSON or file-path outputs from CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to produce saved summaries, markdown compilations, supercut video files, reference sidecars, and still frames through yt-mem-ai commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
