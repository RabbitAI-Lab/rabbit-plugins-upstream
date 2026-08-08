## Description: <br>
Browse, extract, and summarize content from websites or URLs, and search the web for information with support for Chinese interaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agent users can use this skill to ask an agent to visit URLs, summarize webpages, extract webpage content, or search for web information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local read, write, glob, and command-execution authority that is not clearly scoped to browsing tasks. <br>
Mitigation: Review before installing, run only in a sandboxed agent environment, and remove exec/write authority when only web browsing is needed. <br>
Risk: Broad local permissions could expose sensitive workspaces, credentials, or important files. <br>
Mitigation: Do not grant access to sensitive workspaces, credentials, or important files unless the publisher narrows command and file-write behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/web-browsing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown, text, or JSON-style structured responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include extracted webpage content, summaries, search findings, status metadata, and error details.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
