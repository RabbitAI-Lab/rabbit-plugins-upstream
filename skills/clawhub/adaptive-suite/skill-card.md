## Description: <br>
Adaptive Suite provides broad coding, business analysis, project management, web development, data workflow, free resource discovery, and read-only NAS metadata cataloging guidance for Clawdbot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[afajohn](https://clawhub.ai/user/afajohn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and project leads can use this skill for coding assistance, business and project planning, web and data development workflows, free resource discovery, and read-only NAS metadata cataloging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The NAS metadata scraper can catalog file names, metadata, and directory structure from network storage. <br>
Mitigation: Use explicit user-selected directories, exclude sensitive shares, keep results local, and define deletion controls before scanning. <br>
Risk: The skill asks for broad FREE_API_KEYS access without clear service boundaries. <br>
Mitigation: Use separate least-privilege keys for specific named services instead of a shared key bundle. <br>
Risk: Broad coding, analysis, and planning guidance may be incorrect or misleading if applied without review. <br>
Mitigation: Review generated recommendations, code, commands, and configuration before using them in a project or business workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/afajohn/skills/adaptive-suite) <br>
- [Skill homepage](https://docs.molt.bot/tools/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell command, and configuration snippets as needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require local tools such as Python, Node.js, curl, and sqlite3, plus separately scoped API keys for any external services used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
