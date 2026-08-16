## Description:

Analyzes a user's own Xiaohongshu creator-backend metrics, benchmarks recent notes against public high-performing notes on the same topics, and produces an HTML funnel-diagnosis report with concrete improvement actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External Xiaohongshu creators and their agents use this skill to audit recent notes with the creator's logged-in backend analytics, find funnel weaknesses, and compare each note with public high-performing examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's logged-in Chrome Xiaohongshu session and private creator-backend analytics.

Mitigation: Run it only for an account you control and only when you are comfortable granting the agent access to those analytics.

Risk: Prompts containing creator metrics are sent to the configured webclaw3 LLM pipeline endpoint.

Mitigation: Before running, verify WC3_LLM_ENDPOINT is unset or points to a trusted local service.

Risk: Generated Excel, HTML, Markdown, and JSON files may contain sensitive account-performance data.

Mitigation: Store outputs in a controlled directory and review or delete generated files before sharing the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-note-analyst)
- [Project homepage from ClawHub metadata](https://github.com/fatmind/xhs-note-analyst)
- [Required webclaw3 browser automation skill](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [webclaw3 setup guide](https://github.com/fatmind/webclaw3)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [HTML report, Markdown data summary, JSON status summary, and stdout JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may be marked success, partial, or failed; reports and data files can contain private creator-account analytics.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
