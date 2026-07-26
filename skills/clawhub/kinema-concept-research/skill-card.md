## Description: <br>
Research whether a concept has been implemented and its current state using multi-language keywords, multi-engine cross-validation, and multi-dimensional search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeshunee](https://clawhub.ai/user/leeshunee) <br>

### License/Terms of Use: <br>
GNU General Public License v3.0 <br>


## Use Case: <br>
External users, developers, and product researchers use this skill to test whether an idea already has implementations, compare existing tools or approaches, and produce a structured research report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can search the web, clone repositories, download PDFs, and save local research projects. <br>
Mitigation: Ask the agent to confirm before cloning repositories or downloading PDFs, and review downloaded third-party content before executing anything from it. <br>
Risk: Research results from search engines and fetched pages may be incomplete, stale, or misleading. <br>
Mitigation: Use multi-engine cross-validation, inspect high-relevance sources directly, and treat the final report as decision support rather than proof. <br>


## Reference(s): <br>
- [Kinema's Concept Re-Search onboarding](references/ONBOARDING.md) <br>
- [Kinema Concept Re-Search ClawHub page](https://clawhub.ai/leeshunee/skills/kinema-concept-research) <br>
- [searxng-search-cli](https://github.com/KinemaClawWorkspace/searxng-search-cli) <br>
- [Kinema concept research source repository](https://github.com/KinemaClawWorkspace/kinema-concept-research) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown reports and saved local research project files with inline shell commands when setup or search tooling is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local project folders under projects/research-{uuid}/ with concept definitions, keyword notes, search records, cloned repositories or downloaded papers when selected for deep review, and a final report.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
