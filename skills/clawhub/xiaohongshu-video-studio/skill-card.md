## Description:

小红书短视频全解析 turns a Xiaohongshu video link plus a short request into transcripts, summaries, viral-video breakdowns, storyboard scripts, rewritten or original short-video scripts, and reverse-engineered prompts using Cue Omni Reader results and model-based analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and agents use this skill to analyze Xiaohongshu short videos and transform parsed video text into practical creative outputs such as transcripts, structured breakdowns, storyboard tables, scripts, and prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu video links to Cue's remote parsing service and the security summary flags platform, copyright, and anti-scraping concerns.

Mitigation: Use it only for videos the user is authorized to submit, avoid private or restricted links, and review generated outputs for copyright and platform-policy compliance before reuse.

Risk: The security guidance notes local API key handling risk when credentials are stored in plain configuration files.

Mitigation: Prefer CUE_API_KEY or a managed secret store, avoid committing credentials, and do not paste API keys into shared transcripts or artifacts.

Risk: Generated scripts, claims, and commercial content can be inaccurate or legally sensitive.

Mitigation: Review generated scripts before use, verify factual and advertising claims, and avoid unsupported absolute or regulated claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/xiaohongshu-video-studio)
- [Cue Omni Reader](https://cuecue.cn/hub/omni-reader)
- [Cue API Key management](https://cuecue.cn/hub/api-key)
- [Cue payment and credits](https://cuecue.cn/pay)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, tables, scripts, prompts, JSON snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include inferred shot, camera, transition, and emotion fields that should remain labeled as inferred when not present in the parser result.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
