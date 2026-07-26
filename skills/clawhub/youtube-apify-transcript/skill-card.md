## Description: <br>
Fetches YouTube transcripts through the Apify API, including support for cloud IP environments, local caching, batch mode, language preference, and text or JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve transcripts for YouTube videos so the agent can summarize, analyze, or transform video content from transcript text. It is useful in cloud-hosted environments where direct YouTube transcript access may be blocked. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requested YouTube video URLs are sent to Apify to retrieve transcripts. <br>
Mitigation: Use this skill only when sharing those URLs with Apify is acceptable for the user's privacy and compliance requirements. <br>
Risk: Transcript data may be cached locally on disk. <br>
Mitigation: Choose an appropriate cache directory, disable cache when needed, and clear cached transcripts when they should not persist. <br>
Risk: The skill requires an Apify API token and can consume Apify quota for uncached requests. <br>
Mitigation: Use a dedicated token with suitable quota limits and monitor usage for broad or batch transcript requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robbyczgw-cla/skills/youtube-apify-transcript) <br>
- [Apify pricing](https://apify.com/pricing) <br>
- [Apify API token setup](https://console.apify.com/account/integrations) <br>
- [YouTube Transcript Scraper actor](https://apify.com/topaz_sharingan/Youtube-Transcript-Scraper-1) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files, shell commands, guidance] <br>
**Output Format:** [Plain text transcripts, JSON transcript objects, or transcript files written by the command-line script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include timestamps, video metadata, cache status, and batch processing summaries.] <br>

## Skill Version(s): <br>
1.3.3 (source: frontmatter, package.json, CHANGELOG, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
