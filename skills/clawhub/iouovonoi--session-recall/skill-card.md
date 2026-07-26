## Description: <br>
Let your agent proactively recall local Copilot CLI sessions and reconnect past ideas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iouovonoi](https://clawhub.ai/user/iouovonoi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Session Recall to sync their own local Copilot CLI session history into a searchable local index, compare current work against past sessions, and produce concise context, graph, or context-pack outputs when prior work is relevant. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill duplicates and indexes Copilot conversation history into local plaintext files and SQLite data under SessionRecall. <br>
Mitigation: Install only with user consent, keep the SessionRecall folder private, and do not share generated context packs or local memory stores. <br>
Risk: Optional scheduler setup can repeatedly sync local Copilot session history in the background. <br>
Mitigation: Enable the scheduler only when repeated background syncing is intended; otherwise run manual sync commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iouovonoi/skills/session-recall) <br>
- [REFERENCE.md](artifact/REFERENCE.md) <br>
- [Validation notes](artifact/docs/validation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with PowerShell commands and JSON or Markdown tool outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are local-first; compare and report results may include matched session metadata, recommended context, graph JSON, or exported Markdown context packs.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
