## Description: <br>
Customizes safety zones, identifies babies crawling out or approaching dangerous areas such as bedsides/windowsills, and immediately alerts to protect baby safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and caregivers use this skill to analyze home monitoring video or image inputs for virtual fence boundary crossings, dangerous-area approach events, and related infant safety alerts. Agents can also query cloud-hosted historical alert reports and present structured results or report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive baby or household monitoring footage and report data may be sent to a remote cloud service. <br>
Mitigation: Use only approved footage, confirm user consent and data-handling requirements before execution, and avoid submitting private monitoring media unless the destination service is acceptable. <br>
Risk: The skill may silently create or reuse an identity for analysis and history retrieval. <br>
Mitigation: Review identity behavior before installation, verify which account or default identity will be used, and restrict history queries to authorized users. <br>
Risk: Authentication tokens may be stored locally in the workspace database. <br>
Mitigation: Run in a controlled workspace, protect local database files, and rotate or remove stored credentials when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, json, shell commands, files, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis reports, Markdown tables for historical report lists, and optional saved result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local video files or public video URLs, history-list retrieval, basic/standard/json detail levels, and optional output file paths.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
