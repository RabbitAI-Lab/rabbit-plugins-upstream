## Description: <br>
文曲·文库 guides agents through planning, searching, fetching, indexing, and maintaining reusable source libraries for Chinese content creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and content agents use this skill to collect comparable articles and source material, fetch web pages when authorized, and maintain indexed reusable libraries for Chinese writing projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can ask to update wenqu-cli or download a managed browser runtime before enhanced fetching. <br>
Mitigation: Require explicit user authorization for environment-changing setup, and continue with native search or fetching when authorization is declined. <br>
Risk: Research collection can fetch web content and write local material libraries. <br>
Mitigation: Keep original source URLs in the index, review collected material before reuse, and avoid restricted, private, or access-controlled content. <br>
Risk: Search and fetch operations may encounter login, verification, paywall, or empty-content pages. <br>
Mitigation: Record failures visibly and use public alternatives instead of retrying or bypassing access controls. <br>


## Reference(s): <br>
- [Wenqu Library homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-library) <br>
- [Collection playbook](references/collection-playbook.md) <br>
- [Wenqu CLI guide](references/wenqu-cli.md) <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-library) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with indexed tables and optional shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local material files and source index entries when used by an agent.] <br>

## Skill Version(s): <br>
0.1.17 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
