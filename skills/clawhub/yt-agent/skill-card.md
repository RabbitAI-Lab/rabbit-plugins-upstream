## Description: <br>
Generate summaries, highlights, Q&A, presentations, daily digests, or cross-video reviews from YouTube videos using cached transcripts and semantic search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dasein108](https://clawhub.ai/user/dasein108) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content analysts use this skill to turn YouTube videos, channel uploads, subscriptions, and dated video groups into transcript-grounded summaries, highlights, Q&A, slide decks, digests, and reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can configure YouTube access through the user's Chrome browser profile. <br>
Mitigation: Review before installing and require explicit user approval before setting browser-cookie access such as YT_COOKIES_BROWSER=chrome. <br>
Risk: The skill uses unpinned uvx execution for the yt-mem-ai CLI. <br>
Mitigation: Use in a controlled environment and pin or review the CLI package before operational use when reproducibility or supply-chain control matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dasein108/skills/yt-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON snippets, shell commands, and generated Markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write slide decks, digests, reviews, and group syntheses to local Markdown files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
