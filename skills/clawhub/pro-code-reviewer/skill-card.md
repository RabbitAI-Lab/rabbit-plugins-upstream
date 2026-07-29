## Description: <br>
Review code against platform-specific rules for Android and iOS, language-specific rules for TypeScript and Go, and general engineering rules across local diffs, commits, branches, and remote PR URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[timeaground](https://clawhub.ai/user/timeaground) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to review code changes before merge, with structured severity labels, platform-aware checks, and concrete fix guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reviewing a repository can expose code diffs and nearby source context to the AI assistant. <br>
Mitigation: Avoid running the skill on changes containing secrets or highly sensitive proprietary code unless that disclosure is acceptable in the user's environment. <br>
Risk: Automated review findings can be incorrect, incomplete, or overly broad for a codebase's conventions. <br>
Mitigation: Treat findings as review assistance and require a human engineer to confirm issues before making merge or release decisions. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [General Review Rules](references/review-general.md) <br>
- [Android Review Rules](references/review-android.md) <br>
- [iOS Review Rules](references/review-ios.md) <br>
- [TypeScript Review Rules](references/review-typescript.md) <br>
- [Go Review Rules](references/review-go.md) <br>
- [Agent Skill Review Rules](references/review-skill-vetter.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown review findings with severity labels, file locations, explanations, and fix suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include concrete replacement code and commands when relevant to the review finding.] <br>

## Skill Version(s): <br>
1.3.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
