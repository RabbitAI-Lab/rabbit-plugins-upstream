## Description:

老兵知识采集器 enriches an IMA knowledge base by searching Sogou WeChat articles by topic, filtering and encoding candidates, and batch-importing selected article URLs into a specified IMA folder when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byrdsongstratakoslb663-ctrl](https://clawhub.ai/user/byrdsongstratakoslb663-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge-base maintainers and agents use this skill to collect topic-focused WeChat article candidates, prepare deduplicated batches, and import them into a chosen IMA knowledge-base folder after confirming the target knowledge base, folder, and article count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can bulk-import URLs into an IMA knowledge-base folder.

Mitigation: Confirm the exact knowledge base, folder, and article count before import, and inspect generated batches before any import action.

Risk: A helper script uses a hardcoded D:\WorkBuddy path for local reads and writes.

Mitigation: Change or remove the hardcoded path before running the script so all file operations stay in the intended project directory.

Risk: Incorrect imports or noisy articles may require manual cleanup because IMA has no deletion API in the documented workflow.

Mitigation: Review imported titles after completion, generate a cleanup list for unwanted media IDs, and remove bad entries manually in the IMA interface.

## Reference(s):

- [IMA MCP tool signatures and ID baseline](references/ima_kb_api.md)
- [Search and import efficiency review](references/pitfalls.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON batch files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create article candidate lists, filtered URL batches, wave files, import status summaries, and cleanup reports.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
