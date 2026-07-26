## Description: <br>
Forge is a forge-agnostic git-host driver contract that helps agent pipelines reason about GitHub, GitLab, and Gitea PR, issue, merge, visibility, reference, dependency, and review-bot operations through normalized driver methods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation engineers use this skill when designing or updating repository workflow agents that need to operate across GitHub, GitLab, and Gitea. It provides a normalized driver interface, dispatch model, capability matrix, and adapter boundaries so pipelines can choose native behavior or documented degrade paths per forge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use existing GitHub, GitLab, or Gitea CLI authentication when invoked by an agent workflow. <br>
Mitigation: Install and enable it only in repositories where agent-driven issue, PR, MR, and merge operations are intended, and scope CLI credentials to the minimum permissions needed. <br>
Risk: Forge auto-detection falls back to GitHub when the remote host cannot be resolved. <br>
Mitigation: Use an explicit --forge value for non-GitHub or self-hosted repositories when incorrect fallback behavior would be disruptive. <br>
Risk: Some GitLab and Gitea adapter behavior is documented as a Phase 2 boundary rather than complete implementation. <br>
Mitigation: Treat GitLab and Gitea paths as contract guidance unless the consuming pipeline has implemented and tested the corresponding adapter methods. <br>


## Reference(s): <br>
- [Forge skill page](https://clawhub.ai/drumrobot/skills/forge) <br>
- [Publisher profile](https://clawhub.ai/user/drumrobot) <br>
- [Changelog](CHANGELOG.md) <br>
- [Driver Interface](driver-interface.md) <br>
- [Capability Matrix](capability-matrix.md) <br>
- [Dispatch](dispatch.md) <br>
- [Adapters](adapters.md) <br>
- [Initial forge registration issue](https://github.com/es6kr/skills/issues/74) <br>
- [Initial forge registration commit](https://github.com/es6kr/skills/commit/1bb16ea7c7cc466b43c87c0761bc841fe8cab95d) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with normalized method contracts, capability tables, and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a bash driver resource that can assemble or run host CLI commands through gh, glab, or tea depending on forge detection.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and changelog, released 2026-07-07) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
