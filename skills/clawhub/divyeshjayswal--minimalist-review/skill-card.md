## Description: <br>
Review code, a diff, or a PR strictly for bloat: unrequested abstractions, dead scope, dependency creep, symptom-patching, and drive-by changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[divyeshjayswal](https://clawhub.ai/user/divyeshjayswal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill as a terse second-pass review to identify unnecessary abstractions, dead scope, dependency creep, symptom patches, and unrelated changes in code, diffs, or pull requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may bias review toward removing code even when context or requirements justify it. <br>
Mitigation: Treat findings as review guidance and confirm each proposed cut against requirements, correctness, and safety needs. <br>
Risk: Terse findings may omit nuance about validation, authentication, error handling, resource cleanup, or tests. <br>
Mitigation: Preserve safeguards and use the skill's stated priority that missing guards outrank extra lines. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown review findings with file:line recommendations and a verdict] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Terse findings, an estimated LOC floor, and the top three recommended cuts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
