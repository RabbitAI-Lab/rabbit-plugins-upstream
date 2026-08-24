## Description:

Create Bilibili upload copy from a topic, title, outline, or script, then optionally generate one matching 16:9 thumbnail from the settled title and thumbnail brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Bilibili creators and publishing teams use this skill to turn video topics, outlines, or finished scripts into upload-ready titles, descriptions, tags, chapter text, pinned-comment prompts, and thumbnail briefs. After the copy is settled, the skill can prepare and run one approved Beatra thumbnail generation request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad Beatra account permissions, including media-generation and credit-spending scopes.

Mitigation: Install only when those permissions match the intended workflow, run authorization knowingly, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: Prompts and creator content may be sent to Beatra for model and generation tasks.

Mitigation: Review the topic, script, prompt, and thumbnail plan before approval, and avoid including private or sensitive creator content that is not needed for the output.

Risk: Thumbnail generation is paid work and duplicate retries can create avoidable charges.

Mitigation: Require the frozen plan, current estimate, and stable client_request_id before approval; retry uncertain submissions only with the identical request identity and unchanged arguments.

Risk: Installed package code can silently auto-update by default.

Mitigation: Review the auto-update posture before use and disable silent checks with `python3 scripts/mcp_client.py update --auto off` when manual update control is required.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/beatra-ai/skills/bilibili-publishing-pack)
- [Beatra Skill Homepage](https://beatra.ai/skills/bilibili-publishing-pack)
- [Publishing Workflow](references/workflow.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured publishing copy, thumbnail plan details, and optional task result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to Simplified Chinese publishing copy; one paid 2K landscape 16:9 thumbnail may be generated only after explicit approval of the frozen plan and current estimate.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
