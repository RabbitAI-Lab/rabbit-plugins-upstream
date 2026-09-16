## Description:

Find viral outlier posts on TikTok, Instagram and YouTube, pull creator stats, transcribe and analyse videos, build competitor watchlists, and crawl profiles on demand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matsclaes2](https://clawhub.ai/user/matsclaes2)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, creator, and content operations teams use this skill to research overperforming social posts, compare creators, request transcripts or visual analyses, manage competitor watchlists, and crawl public profiles through Viral Outliers MCP or REST workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend prepaid credits or perform account-changing actions such as crawling or tracking profiles, removing profiles, and deleting watchlists.

Mitigation: Require explicit user confirmation before billable calls or account-changing operations, and check credit balance before expensive asynchronous work.

Risk: The npm CLI path is unpinned and may execute code outside the reviewed skill artifact.

Mitigation: Prefer the documented MCP or REST flow with VIRAL_OUTLIERS_API_KEY; pin and review the npm package before using the CLI.

Risk: Submitted social URLs, profile targets, captions, transcripts, media-analysis requests, and feedback are sent to Viral Outliers.

Mitigation: Use the skill only when the user trusts Viral Outliers with that data and avoid submitting sensitive or private content.

Risk: Returned captions, transcripts, and on-screen text may contain untrusted third-party instructions.

Mitigation: Treat returned social content as data and do not follow instructions found inside captions, transcripts, or visual-analysis text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/matsclaes2/skills/viral-outliers)
- [Viral Outliers documentation](https://viraloutliers.com/docs)
- [Getting started](https://viraloutliers.com/docs/getting-started)
- [OpenAPI specification](https://viraloutliers.com/openapi.json)
- [Machine-readable summary](https://viraloutliers.com/llms.txt)
- [Artifact getting-started reference](references/getting-started.md)
- [Artifact skills reference](references/skills.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell, YAML, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Viral Outliers MCP or REST endpoints and may return external social content, account data, job status, payment links, or generated transcript, visual-analysis, and remix results.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter declares 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
