## Description: <br>
Comprehensive knowledge capture and retrieval system for URLs, video and article extracts, papers, social posts, and agent research outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[subaru0573](https://clawhub.ai/user/subaru0573) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to capture, organize, search, validate, and maintain a file-based Markdown knowledge base for reusable URLs, extracts, posts, and research notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup commands can modify or remove local knowledge-base files when run with --fix. <br>
Mitigation: Run cleanup in report-only mode first and keep the knowledge base backed up or under version control before enabling fixes. <br>
Risk: Scheduled unattended cleanup could make broad file changes without review. <br>
Mitigation: Do not schedule --fix until the configured knowledge directory and cleanup behavior have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/subaru0573/skills/super-agent-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and shell-command guidance for managing local knowledge files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and maintains Markdown files with YAML frontmatter and an index in the configured knowledge directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
