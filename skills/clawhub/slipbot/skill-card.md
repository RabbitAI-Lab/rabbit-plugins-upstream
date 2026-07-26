## Description: <br>
Used to capture and organize notes, ideas, quotes, and journal entries with automatic tagging, linking, and knowledge graph maintenance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jrswab](https://clawhub.ai/user/jrswab) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use SlipBot to capture prefixed notes, ideas, quotes, and journal entries into a local slipbox, then maintain tags, bidirectional links, and a JSON knowledge graph for later querying. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messages that begin with SlipBot's capture prefixes may be saved unintentionally to the local slipbox. <br>
Mitigation: Run it from the intended workspace and avoid using capture prefixes for unrelated or sensitive messages. <br>
Risk: Automatic note validation and graph cleanup can alter local note metadata and the graph index. <br>
Mitigation: Review or back up the slipbox before relying on automatic graph cleanup. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, configuration] <br>
**Output Format:** [Markdown note files, JSON graph index updates, and concise text responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates local slipbox files when capture prefixes are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
