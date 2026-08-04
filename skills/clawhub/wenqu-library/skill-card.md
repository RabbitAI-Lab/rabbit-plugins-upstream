## Description: <br>
文曲·文库 guides agents through evidence-driven Chinese writing material collection, including scope planning, source search, page fetching, evidence indexing, and reusable material library maintenance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and content teams use this skill to collect, download, index, and reuse source material for Chinese articles, reports, tutorials, project descriptions, and documentation. It is intended for scoped research and writing workflows where each material item preserves a source URL or local path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can search the web and fetch public pages, which may collect irrelevant, low-quality, restricted, or inaccessible material if the scope is too broad. <br>
Mitigation: Confirm the collection scope before searching, prefer source quality during candidate ranking, preserve source URLs, set explicit page limits for site fetches, and record failures instead of bypassing access controls. <br>
Risk: The workflow may install a pinned CLI and, when needed, a browser runtime before managed search or fetch operations. <br>
Mitigation: Request explicit user approval before installation or browser setup, use the documented pinned version, preview browser setup with a dry run, and run the documented health check before use. <br>
Risk: The workflow writes material indexes and reusable library entries under the current project and the user's home directory. <br>
Mitigation: Confirm that the user wants a reusable writing-material library, keep writes limited to the documented material-library paths, and preserve provenance fields for later review. <br>


## Reference(s): <br>
- [Collection playbook](references/collection-playbook.md) <br>
- [Wenqu CLI reference](references/wenqu-cli.md) <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-library) <br>
- [OpenClaw homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-library) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown tables, indexed material files, concise status text, and inline shell commands when CLI setup or fetch steps are needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write material indexes under the project materials directory and reusable entries under $HOME/.gogoingai/wenqu-skills/library/ after the collection scope and required setup are confirmed.] <br>

## Skill Version(s): <br>
0.1.19 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
