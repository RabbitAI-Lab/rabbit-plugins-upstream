## Description: <br>
Loom Workflow analyzes Loom recordings and turns recorded business processes into structured workflow analysis, summaries, and draft automation files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g9pedro](https://clawhub.ai/user/g9pedro) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to analyze authorized Loom walkthroughs, extract workflow steps, identify decision points and ambiguities, and generate draft Lobster automations for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated browser, email, or message workflows may perform incorrect or unintended actions if run without reliable approval gates. <br>
Mitigation: Review generated Lobster files manually, require explicit approvals for external or destructive actions, and use dry-run execution before live use. <br>
Risk: Loom recordings, extracted frames, transcripts, and local test metadata may contain sensitive business or personal information. <br>
Mitigation: Process only recordings the user is authorized to analyze, use approved transcription and vision providers, and delete local outputs when analysis is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g9pedro/skills/loom-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [JSON workflow analysis, Markdown summaries, Lobster YAML files, and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated automation should be reviewed and dry-run before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
