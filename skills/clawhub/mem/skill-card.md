## Description: <br>
Search local memory index (local-first). Use for /mem queries in Telegram. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trumppo](https://clawhub.ai/user/trumppo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to run local-first memory searches for /mem-style Telegram queries and summarize the top indexed hits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill invokes local helper scripts that are not included in the package. <br>
Mitigation: Verify scripts/index-memory.py and scripts/search-memory.py on the target machine before running the workflow. <br>
Risk: The local memory index may contain secrets or private folders that could be surfaced in chat summaries. <br>
Mitigation: Review the indexed locations and exclude sensitive paths before using or summarizing search results. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Markdown or plain text with local shell command examples and summarized search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns top hits with paths and headers; summaries are brief when needed.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
