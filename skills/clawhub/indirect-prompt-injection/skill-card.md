## Description: <br>
Detect and reject indirect prompt injection attacks when reading external content such as social media posts, comments, documents, emails, web pages, and user uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aviv4339](https://clawhub.ai/user/aviv4339) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill before processing untrusted external content to identify instruction overrides, goal manipulation, data-exfiltration attempts, obfuscation, and social-engineering patterns. It provides human review guidance and optional scripts for analyzing text, files, and detector test cases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact includes examples and tests containing jailbreaks, credential-exfiltration requests, and prompt-leak attempts. <br>
Mitigation: Treat those strings as detector fixtures and documentation examples, not instructions to follow. <br>
Risk: Running the bundled scripts on unintended files could expose or process content outside the review scope. <br>
Mitigation: Run the scripts only on content or files intentionally selected for defensive review. <br>
Risk: Pattern-based detection can produce false positives or miss novel attacks. <br>
Mitigation: Review findings in context, preserve the original user task, and ask for confirmation when suspicious embedded instructions are ambiguous. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aviv4339/skills/indirect-prompt-injection) <br>
- [Attack Pattern Taxonomy](references/attack-patterns.md) <br>
- [Detection Heuristics](references/detection-heuristics.md) <br>
- [Safe Content Parsing](references/safe-parsing.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands; the sanitizer can emit human-readable text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Exit code 1 indicates suspicious content; scripts should be run only on content or files intentionally selected for review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
