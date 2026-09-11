## Description:

事实核查 uses Cue to cross-check claims against independent sources and underlying data, identifying stale timelines, data discrepancies, and misleading statements in a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to submit news, research-report claims, diligence materials, or market rumors for structured fact checking with source comparisons and correction evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fact-checking content is sent to the external Cue service and external data sources.

Mitigation: Do not submit secrets, regulated data, or nonpublic business material unless that use of Cue is approved.

Risk: The skill relies on a Cue API key stored in ~/.cue/config.json or provided through CUE_API_KEY.

Mitigation: Protect the API key, avoid exposing it in prompts or logs, and rotate it if disclosure is suspected.

Risk: The artifact tells the agent that mid-run cancellation is prohibited once the Cue run starts.

Mitigation: Confirm the user accepts the expected 2-15 minute run before launch and avoid unattended execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fact-check)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Example fact-check report](https://cuecue.cn/share/680abf29664d)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Structured Markdown report with source links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be saved under ~/cue-reports and converted to DOCX or PDF with pandoc.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
