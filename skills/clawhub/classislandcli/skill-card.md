## Description: <br>
ClassIsland timetable command-line assistant for querying and managing subjects, time layouts, class plans, and course order changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qibowen2008](https://clawhub.ai/user/qibowen2008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, teachers, and ClassIsland users can ask an agent to inspect or update ClassIsland timetable data through ClassIslandCLI, including subjects, time layouts, class plans, and temporary or permanent course swaps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change ClassIsland timetable data through deletion, overwrite, and permanent course-swap operations. <br>
Mitigation: Review the requested action, confirm the target profile or timetable, and allow destructive changes only when explicitly requested and recoverable. <br>
Risk: The skill exposes installation commands for shell completions and WorkBuddy skills that can alter the user's agent or shell environment. <br>
Mitigation: Do not allow it to install completions, install skills, or overwrite existing skills unless the user explicitly requested that exact action and trusts the source. <br>


## Reference(s): <br>
- [ClassIslandCLI releases API](https://gitee.com/api/v5/repos/buger2008/ClassIslandCLI/releases?page=1&per_page=20&direction=desc) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language text with JSON-derived summaries and inline command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may read or modify ClassIsland profile, subject, timetable, and class-plan data.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence; artifact frontmatter: 1.0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
