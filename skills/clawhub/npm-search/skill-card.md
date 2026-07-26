## Description: <br>
Search npm packages for Node.js and JavaScript packages, libraries, and tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to search and discover npm packages relevant to a Node.js or JavaScript task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks the agent to execute a local npm search helper script that is not included in the available artifact evidence. <br>
Mitigation: Before installing or running the skill, confirm that the package includes scripts/npmsearch and review it for unexpected file access, credential handling, or network calls outside npm package metadata lookup. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and npm-search-mcp-server; commands should substitute the user's package query.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
