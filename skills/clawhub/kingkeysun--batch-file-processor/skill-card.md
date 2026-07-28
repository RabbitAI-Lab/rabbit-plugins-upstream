## Description: <br>
Batch File Processor helps agents process large file sets in parallel with sub-agents for summarization, analysis, extraction, transformation, classification, and code analysis tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kingkeysun](https://clawhub.ai/user/kingkeysun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run the same file-processing task across many files in a selected directory, then compile summaries, extracted JSON, classifications, code-analysis results, or reports from the batched results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch processing sensitive folders can expose secrets, credentials, private customer data, or personal files in summaries or extracted JSON. <br>
Mitigation: Select narrow directories and file patterns, exclude sensitive files, and add redaction before processing confidential content. <br>
Risk: Oversized batches or whole-directory processing can cause context overflow, timeouts, or incomplete summaries. <br>
Mitigation: Use the documented 2-4 files per sub-agent batching pattern and increase timeouts only for large files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kingkeysun/skills/batch-file-processor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, task templates, and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Sub-agent batches typically process 2-4 files and return standardized JSON for aggregation.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
