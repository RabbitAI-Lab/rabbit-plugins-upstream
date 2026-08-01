## Description: <br>
Converts user-provided web links or local files into structured Markdown and stores the result in configured Obsidian, Feishu Cloud Drive, and Tencent IMA Knowledge Base destinations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and agents use this skill when a user explicitly asks to convert selected web or local content into Markdown and save it to one or more configured knowledge destinations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-selected web content, private URLs, or local files may be written locally or sent to Feishu and Tencent IMA. <br>
Mitigation: Use the skill only for content approved for the configured destinations, and use --no-feishu, --no-ima, --no-obsidian, or --dry-run when only conversion or a subset of storage targets is intended. <br>
Risk: Feishu uploads use the currently authenticated lark-cli user account. <br>
Mitigation: Verify the active lark-cli account before running storage workflows. <br>
Risk: Dependency behavior may change if Python packages are installed without version controls. <br>
Mitigation: Pin and update dependencies through the user's managed environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardwason/skills/web-to-fim) <br>
- [README.en.md](README.en.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>
- [Tencent IMA Knowledge Base API Setup](references/ima-setup.md) <br>
- [Feishu Cloud Document Block Mapping](references/feishu-blocks.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown files, local or cloud storage actions, and concise command/configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write Markdown with frontmatter to an Obsidian vault, upload Markdown files to Feishu Cloud Drive, and create or import content in Tencent IMA based on user-selected destinations.] <br>

## Skill Version(s): <br>
3.7.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
