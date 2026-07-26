## Description: <br>
Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivansslo](https://clawhub.ai/user/ivansslo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to investigate bugs, test failures, build failures, performance problems, and integration issues through a structured root-cause workflow before proposing fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagnostic examples can expose environment values or macOS keychain signing identity metadata in shared logs. <br>
Mitigation: Adapt diagnostic commands before use, redact environment values, avoid dumping keychain or signing identity details into shared logs, and require explicit approval before credential- or identity-related diagnostics. <br>
Risk: The skill uses broad, forceful process instructions that may over-constrain debugging behavior if followed without judgment. <br>
Mitigation: Review before installing and treat the process as guidance that must be adapted to the specific debugging context. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/ivansslo/Supwrs/tree/main/skills/systematic-debugging) <br>
- [ClawHub skill page](https://clawhub.ai/ivansslo/skills/systematic-debugging) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with checklists and example shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
