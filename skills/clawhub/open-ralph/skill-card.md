## Description: <br>
Run an autonomous Open Ralph Wiggum coding loop using OpenCode Zen with free models and automatic fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bderiel](https://clawhub.ai/user/bderiel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to run bounded autonomous coding loops for fixing tests, implementing scoped features, refactoring, and resolving lint, type, or build failures inside a git repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The autonomous coding loop may change files in the current repository. <br>
Mitigation: Run it on a clean branch or worktree and review the full git diff before committing or merging. <br>
Risk: Large iteration limits can create runaway or overly broad coding sessions. <br>
Mitigation: Keep iteration limits conservative and provide verifiable success criteria in the prompt. <br>
Risk: Using OpenCode or provider-hosted models may expose repository content to provider processing. <br>
Mitigation: Avoid confidential code unless the relevant OpenCode and provider processing terms are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bderiel/skills/open-ralph) <br>
- [Project homepage](https://github.com/Th0rgal/open-ralph-wiggum) <br>
- [OpenCode Zen models](https://opencode.ai/zen/v1/models) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces prompts and command options for a bounded autonomous coding loop with model fallback guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
