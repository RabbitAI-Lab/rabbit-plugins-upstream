## Description: <br>
Extract transcripts, summaries, and metadata from YouTube videos for content repurposing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketers, developers, and agents use this skill to fetch YouTube transcripts, generate simple summaries, pull metadata, and repurpose video content into text workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI makes outbound requests to YouTube and Invidious to retrieve transcripts, metadata, and search results. <br>
Mitigation: Install and run it only in environments where those network requests are acceptable, and review retrieved content before reuse. <br>
Risk: The bundled CI verifier is intended for deliberate local or CI checks and can be risky on untrusted folders. <br>
Mitigation: Run the verifier only on trusted or isolated folders and keep secrets and sensitive files outside scanned workspaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/youtube-content) <br>
- [Publisher profile](https://clawhub.ai/user/itspremkumar) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and text outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Transcript output is truncated by the CLI after 5000 characters; summary output is extractive text derived from retrieved captions.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
