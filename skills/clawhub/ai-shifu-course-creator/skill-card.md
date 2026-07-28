## Description: <br>
AI-Shifu Course Creator helps agents create, edit, optimize, deploy, manage, and analyze AI-Shifu courses using MarkdownFlow Teaching Prompts and Course Prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heshaofu2](https://clawhub.ai/user/heshaofu2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External course authors and operators use this skill to turn source material into AI-Shifu course artifacts, deploy or update courses, manage learner-facing course settings, and review live course analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores AI-Shifu login tokens for authenticated platform operations. <br>
Mitigation: Install only for accounts where this access is acceptable, review saved-token handling, and remove or rotate credentials when access is no longer needed. <br>
Risk: Account-linked usage telemetry is sent by default. <br>
Mitigation: Review telemetry behavior before use and set AI_SHIFU_SKILL_TELEMETRY=off when telemetry should be disabled. <br>
Risk: Course import, publish, archive, delete, and reorder operations can affect learner-facing courses. <br>
Mitigation: Use the documented pull, status, preview, export, and verification steps before and after mutations, and require explicit confirmation for high-impact changes. <br>


## Reference(s): <br>
- [Skill definition](SKILL.md) <br>
- [Platform authentication](references/authentication.md) <br>
- [Course design intake](references/course-design-intake.md) <br>
- [Teaching Prompt authoring](references/teaching-prompt.md) <br>
- [Course Prompt authoring](references/course-prompt.md) <br>
- [Deployment workflow](references/deployment-workflow.md) <br>
- [Existing course sync](references/course-sync.md) <br>
- [Course management](references/course-management.md) <br>
- [Analytics overview](references/analytics/overview.md) <br>
- [CLI reference](references/cli/cli-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose with command snippets, MarkdownFlow course files, JSON analytics queries, and local course artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local course directories and invoke AI-Shifu platform commands when authenticated.] <br>

## Skill Version(s): <br>
1.2.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
