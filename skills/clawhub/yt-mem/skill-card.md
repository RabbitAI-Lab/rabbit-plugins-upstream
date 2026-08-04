## Description: <br>
Guides an agent through yt-mem-ai CLI operations for ingesting YouTube videos, discovering subscription uploads, searching a local library, saving summaries, generating recommendations, compiling highlights, and producing supercuts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dasein108](https://clawhub.ai/user/dasein108) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to have an agent operate a local YouTube memory workflow through the yt-mem-ai CLI, including ingestion, transcript search, summaries, recommendations, highlights, and video output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to download media, store transcripts and embeddings locally, and create persistent output files. <br>
Mitigation: Run it only in workspaces where local media, transcripts, embeddings, and generated files are acceptable, and review reported file paths after execution. <br>
Risk: Blocked YouTube fetches may require browser cookies or proxy credentials. <br>
Mitigation: Configure cookies or proxy credentials only when needed, use the CLI configuration commands rather than ad hoc environment variables, and avoid revealing stored secrets unless explicitly required. <br>
Risk: Generated summaries and highlight timestamps can be inaccurate if the agent writes analysis without anchoring it in stored transcripts. <br>
Mitigation: Use the CLI to read stored transcripts and search for supporting phrases before saving summaries or timestamped highlights. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dasein108/skills/yt-mem) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference generated local artifacts such as digests, compilations, supercuts, frames, and sidecar reference files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
