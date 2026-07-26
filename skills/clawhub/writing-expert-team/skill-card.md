## Description: <br>
Writing Expert Team coordinates a multi-role writing workflow for style profiling, topic planning, research, drafting, fact-checking, legal and compliance review, editing, and platform-specific formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lawer-liu](https://clawhub.ai/user/lawer-liu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketers, and subject-matter writers use this skill to plan, draft, review, and format articles for social, legal, science communication, and other compliance-sensitive publishing workflows. It supports both full-pipeline execution and targeted help from individual writing roles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated articles, legal references, or compliance judgments may be incorrect, outdated, or unsuitable for publication. <br>
Mitigation: Review generated content before publication and use the skill's fact-checking, legal review, and user confirmation steps before formatting or publishing. <br>
Risk: Optional publishing workflows may interact with WeChat tools or publishing credentials when the user configures them. <br>
Mitigation: Keep API credentials in the publishing tool's configuration, enable draft push only by explicit user request, and manually review previews before publishing. <br>
Risk: The redline checker can modify Markdown or text files when run with --fix. <br>
Mitigation: Run --fix only on files intended for modification and review the resulting changes before using the output. <br>
Risk: The workflow may create local draft, state, preview, or export files during article production. <br>
Mitigation: Use a project-specific workspace and inspect generated files before sharing or committing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lawer-liu/skills/writing-expert-team) <br>
- [README](README.md) <br>
- [Role definitions](references/roles.md) <br>
- [Pipeline flow](references/pipeline-flow.md) <br>
- [Metadata schema](references/metadata-schema.md) <br>
- [Publishing redlines](references/redlines.md) <br>
- [Viral article formula](references/viral_formula.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and text responses with YAML metadata blocks, optional HTML or file-oriented publishing artifacts, and shell commands for redline checks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local draft or state files and may interact with WeChat publishing tools only when explicitly configured by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
