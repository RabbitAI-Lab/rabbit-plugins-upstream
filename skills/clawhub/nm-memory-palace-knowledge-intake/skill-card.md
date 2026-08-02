## Description: <br>
Processes external resources into stored knowledge with quality scoring and routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to evaluate linked articles, papers, documents, and local files, then route useful material into a persistent knowledge corpus with validation, promotion, application, and pruning guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to store, publish, or apply externally sourced content in persistent knowledge bases. <br>
Mitigation: Review each write, publication, code or skill change, and queue-processing action before execution. <br>
Risk: Private or sensitive content may be captured in a corpus, queue, drafts, logs, or GitHub Discussions. <br>
Mitigation: Avoid sensitive inputs unless storage destinations and publication targets have been checked and approved. <br>
Risk: Automation such as auto-accept can apply intake decisions without enough review. <br>
Mitigation: Require explicit approval before enabling auto-accept or similar automation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-memory-palace-knowledge-intake) <br>
- [OpenClaw Memory Palace Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace) <br>
- [About the KonMari Method](https://konmari.com/about-the-konmari-method/) <br>
- [Rule 6: Ask Yourself If It Sparks Joy](https://konmari.com/marie-kondo-rules-of-tidying-sparks-joy/) <br>
- [Why the KonMari Method Works](https://konmari.com/what-is-konmari-method/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured templates and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose corpus entries, GitHub Discussion summaries, storage templates, and pruning actions that require human review.] <br>

## Skill Version(s): <br>
1.9.17 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
