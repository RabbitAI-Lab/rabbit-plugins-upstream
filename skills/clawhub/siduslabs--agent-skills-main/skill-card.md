## Description: <br>
GitHub PR/issue agent transcripts: redact, preview, and insert safely. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[siduslabs](https://clawhub.ai/user/siduslabs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill during GitHub PR and issue workflows to find local agent session logs, render a sanitized transcript, preview it, and insert only approved relevant context into the body. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanned artifact bundles unrelated high-authority skills and install guidance beyond the published transcript workflow. <br>
Mitigation: Install only the intended agent-transcript skill from a clean package or source path, and do not bulk-enable the nested repository unless those broader workflows are also desired. <br>
Risk: Agent session logs can contain secrets, private data, unrelated work, or overly broad local paths. <br>
Mitigation: Use the skill's local-only redaction, fail-closed checks, trimming, and user approval workflow before adding any transcript to a public PR or issue body. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/siduslabs/skills/agent-skills-main) <br>
- [Agent Transcript skill definition](artifact/SKILL.md) <br>
- [OpenClaw Agent Skills README](artifact/agent-skills-main/README.md) <br>
- [OpenClaw Agent Skills Vision](artifact/agent-skills-main/VISION.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown transcript sections, local HTML previews, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-only workflow; sanitized transcript output is reviewed before insertion.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
