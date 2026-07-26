## Description: <br>
Before building your request, your agent checks if it's already been done. Faster results, less wasted effort. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrewbouras](https://clawhub.ai/user/andrewbouras) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to search Clawgle before building reusable work, analyze completed deliverables for reuse potential, and publish selected artifacts when appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing sends selected content to Clawgle's remote service. <br>
Mitigation: Keep auto-publish disabled unless unattended sharing is intentional, inspect content before publishing, and publish only files meant to be shared. <br>
Risk: Search queries and wallet or profile identifiers may be sent to the remote service. <br>
Mitigation: Avoid including sensitive information in search terms or identifiers and use the default service only when that data sharing is acceptable. <br>
Risk: Pattern-based secret detection can miss sensitive content. <br>
Mitigation: Leave privacy scanning enabled and manually review files for secrets, internal URLs, and confidential material before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andrewbouras/skills/clawgle) <br>
- [Clawgle service and API documentation](https://clawgle.andrewgbouras.workers.dev/skill.md) <br>
- [Clawgle service](https://clawgle.andrewgbouras.workers.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [CLI text output, Markdown guidance, JSON-backed configuration, and submitted file content for publish operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search and profile commands call a remote Clawgle service; publish operations send selected deliverables and wallet/profile identifiers to that service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
