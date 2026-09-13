## Description:

Analyzes a user's own Xiaohongshu creator-backend metrics, compares notes against public high-performing posts, and produces a local HTML account-diagnosis report with funnel health checks and improvement actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to review their own Xiaohongshu account performance, identify funnel weak points across click-through, retention, engagement, and follower conversion, and generate concrete next-post improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates through a logged-in Xiaohongshu creator session and handles sensitive account analytics.

Mitigation: Run it only in a trusted local environment, confirm the browser session is the intended account, and remove exported spreadsheets and generated reports when they contain sensitive data.

Risk: Prompts and account-performance details may be sent to the configured webclaw3 pipeline endpoint.

Mitigation: Keep WC3_LLM_ENDPOINT pointed at a trusted local or approved endpoint before running the skill.

Risk: The artifact includes an obfuscated LLM helper file identified in the security guidance.

Mitigation: Review or replace wc3-code.mjs before deployment in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-note-analyst)
- [Project homepage](https://github.com/fatmind/xhs-note-analyst)
- [webclaw3 browser automation dependency](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [webclaw3 installation guide](https://github.com/fatmind/webclaw3)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, files]

**Output Format:** [HTML report, JSON status summary, Markdown data file, and stdout JSON summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local report_path HTML file, res.json, and data.md; results may be partial when enough high-quality benchmark posts are unavailable.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
