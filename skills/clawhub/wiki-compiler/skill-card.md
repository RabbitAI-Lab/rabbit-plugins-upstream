## Description: <br>
Organizes raw materials in Tencent IMA into structured wiki-style knowledge bases with folder classification, guide-note generation, tagging, and maintenance workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cookfish1979](https://clawhub.ai/user/cookfish1979) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and knowledge-base maintainers use this skill to turn Tencent IMA source materials into navigable wiki guides, organize scattered files into folder structures, manage tags, and maintain existing knowledge bases over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real Tencent IMA knowledge-base changes when API credentials are available. <br>
Mitigation: Review proposed source lists, destination knowledge base IDs, folder IDs, note IDs, and tag changes before approving write operations. <br>
Risk: Knowledge-base moves, note deletion, tag deletion, and tag renaming can remove or reorganize user content in ways that are difficult to reverse. <br>
Mitigation: Use the documented backup, verification, and explicit confirmation steps before destructive or bulk operations, and prefer preserving old notes when possible. <br>
Risk: Processing confidential or regulated content may expose that content to Tencent IMA, web search, or LLM processing paths. <br>
Mitigation: Run the skill on sensitive data only when those services and workflows are approved for the data involved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cookfish1979/skills/wiki-compiler) <br>
- [API reference](references/api-reference.md) <br>
- [Folder organization](references/folder-organization.md) <br>
- [Link handling](references/link-handling.md) <br>
- [Write and verify](references/write-and-verify.md) <br>
- [Security guidance](references/security.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell, Python, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed API write operations, confirmation checkpoints, and verification steps.] <br>

## Skill Version(s): <br>
4.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
