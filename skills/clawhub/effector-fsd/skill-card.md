## Description: <br>
Use when designing, reviewing, generating, or refactoring Feature-Sliced Design project structure for Effector ecosystem applications: layers, slices, segments, public APIs, imports, placement of Effector models, Farfetched operations, Atomic Router routes, Next.js adapters, and Steiger checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[demark-pro](https://clawhub.ai/user/demark-pro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to decide and audit Feature-Sliced Design structure for Effector, Farfetched, Atomic Router, and Next.js projects. It helps place models, APIs, routes, public APIs, imports, and review findings under the correct FSD ownership boundary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest adding or running Steiger/FSD lint tooling in a project. <br>
Mitigation: Review generated commands and configuration changes before running them, especially in repositories with existing lint or build pipelines. <br>
Risk: Architecture guidance can lead to incorrect code movement if applied without project context. <br>
Mitigation: Apply recommendations through normal code review and verify behavior with type checks, lint checks, tests, and route-level smoke testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/demark-pro/skills/effector-fsd) <br>
- [Source policy](artifact/references/00-source-policy.md) <br>
- [FSD core rules for Effector projects](artifact/references/01-core-rules.md) <br>
- [Effector placement rules in FSD](artifact/references/02-effector-placement.md) <br>
- [Farfetched placement in FSD](artifact/references/05-farfetched-placement.md) <br>
- [FSD + Effector review checklist](artifact/references/07-review-checklist.md) <br>
- [Effector audit ownership in FSD](artifact/references/11-effector-audit-ownership.md) <br>
- [Feature-Sliced Design documentation](https://feature-sliced.design/) <br>
- [Effector documentation](https://effector.dev) <br>
- [Farfetched documentation](https://ff.effector.dev) <br>
- [Steiger](https://github.com/feature-sliced/steiger) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with folder trees, TypeScript examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend project file review and Steiger/FSD lint tooling; review suggested commands before running them.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
