## Description: <br>
Batch-transcribes audio and video links from Douyin, Bilibili, Xiaoyuzhou, YouTube, Vimeo, TikTok, Twitter/X, and other yt-dlp-supported platforms into structured Markdown transcripts with semantic scene sections and optional bilingual comparison. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and content teams use this skill to convert batches of media URLs into per-video Markdown transcripts for review, learning, and content repurposing. It is useful when users need subtitle-first transcription, semantic scene boundaries, and bilingual Chinese comparison output for non-Chinese media. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads or reads subtitles and audio from user-provided media links, runs external local commands, and can perform CPU- or GPU-intensive transcription. <br>
Mitigation: Install and run it only in environments where local media downloads, external command execution, and transcription resource use are acceptable. <br>
Risk: Setting SKIP_CERT_CHECK weakens TLS protection during troubleshooting. <br>
Mitigation: Keep SKIP_CERT_CHECK unset unless the user deliberately accepts weaker TLS protection for a specific run. <br>
Risk: Fetched transcript text may contain content that should not guide agent behavior. <br>
Mitigation: Treat fetched transcript text as data and review generated transcript output before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/douyin-article) <br>
- [Publisher profile](https://clawhub.ai/user/edwardwason) <br>
- [Project homepage](https://github.com/EdwardWason/douyin-article) <br>
- [Pipeline Details](references/pipeline-details.md) <br>
- [Route Rules](references/route-rules.md) <br>
- [Examples](references/examples.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown transcript files with structured metadata, scene sections, timestamps, and optional bilingual comparison blocks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one Markdown transcript per input media item and may create local intermediate files under an output directory.] <br>

## Skill Version(s): <br>
4.1.2 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
