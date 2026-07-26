## Description: <br>
Remove AI-generated jargon and restore human voice to text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itsflow](https://clawhub.ai/user/itsflow) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Writers, editors, and content teams use this skill to rewrite a named text file so common AI-generated phrasing, hedging, and corporate jargon are replaced with a more natural human voice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent reads the named file and creates a rewritten copy, which may expose sensitive source text to the agent workflow. <br>
Mitigation: Use the skill only with files you are comfortable having the agent read, and avoid confidential, legal, academic, or brand-sensitive writing unless appropriate review controls are in place. <br>
Risk: The rewritten output may change tone, meaning, or factual nuance while removing AI-like phrasing. <br>
Mitigation: Review the -HUMAN output and change log before publishing or relying on the rewritten text. <br>
Risk: A similarly named output file could already exist. <br>
Mitigation: Confirm overwrite behavior or preserve a backup before running the skill where a -HUMAN copy may already be present. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [A rewritten text file plus Markdown-style change log and suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a new copy with a -HUMAN suffix and asks the user to review the result before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
