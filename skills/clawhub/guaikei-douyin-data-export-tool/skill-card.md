## Description:

Collects public Douyin search results, creator posts, video comments, and hot-list data for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to export structured JSON from public Douyin searches, creator profiles, video comments, and real-time hot lists for marketing research, content planning, competitor monitoring, and public sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill sends Douyin queries, Douyin URLs, and GUAIKEI_API_TOKEN to www.guaikei.com.

Mitigation: Install and run it only when that data sharing is acceptable; use a dedicated token and avoid sensitive or private inputs.

Risk: The security review says results are saved automatically in the skill's logs directory.

Mitigation: Review and clear generated logs according to the user's data-retention policy, especially after research involving people, brands, or campaign topics.

Risk: The security review says the activation scope needs review for ambiguous research requests.

Mitigation: Invoke it only when the user clearly wants Douyin or public short-video data, and ask for clarification when the platform or data source is ambiguous.

Risk: The security review says returned results may include media playback or download URLs even though downloading is out of scope.

Mitigation: Use returned URLs as research metadata only; do not use the skill for downloading, redistribution, or rights-infringing workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-export-tool)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Post CLI request schema](assets/post_cli_req.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Comment CLI request schema](assets/comment_cli_req.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot-list CLI response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON on stdout with logs and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and GUAIKEI_API_TOKEN; supports search, post, comment, and hot-list command flows.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
