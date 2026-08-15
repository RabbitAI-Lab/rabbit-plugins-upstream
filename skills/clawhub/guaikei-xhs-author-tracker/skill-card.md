## Description:

This skill helps agents run Node.js CLIs that retrieve public Xiaohongshu search results, note details, author posts, and comments for structured content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, content teams, and market analysts use this skill to collect public Xiaohongshu data for topic research, competitor monitoring, KOL screening, comment analysis, and report preparation. It requires a GUAIKEI_API_TOKEN and should be used only for public data collection within the user's authorization scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release description can understate the skill's actual scope because the artifact includes keyword search, note detail retrieval, author/profile monitoring, and comment collection.

Mitigation: Review the broader Xiaohongshu data-collection scope before installation and disclose the enabled commands to users who expect comment-only behavior.

Risk: User-supplied keywords, note URLs, profile URLs, and token-backed requests are sent to www.guaikei.com.

Mitigation: Use only authorized public Xiaohongshu inputs, avoid private or sensitive monitoring, and confirm that external API processing is acceptable for the deployment.

Risk: Returned data is automatically saved locally under logs/.

Mitigation: Treat saved outputs as collected user data, restrict local access, and clear logs when they are no longer needed.

## Reference(s):

- [Options and CLI usage](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results may be saved locally under logs/ and can be used for downstream summaries, clustering, comparisons, or reports.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
