## Description: <br>
Forge is an autonomous quality engineering swarm for behavioral verification, end-to-end testing, quality gates, and self-healing fix loops across multiple software architectures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ikennaokpala](https://clawhub.ai/user/ikennaokpala) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use Forge to coordinate automated behavioral verification, E2E testing, failure analysis, code fixes, quality gate checks, and learning workflows for software projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Forge gives agents broad local authority to run project commands, start services, run migrations, seed data, edit files, and create commits. <br>
Mitigation: Start with verify-only mode, use a disposable branch or worktree with non-production data, review forge.config.yaml and discovered commands, and inspect diffs, commits, logs, and memory state after each run. <br>
Risk: Automated fixes and commits can introduce incorrect code changes or misleading test confidence. <br>
Mitigation: Review all generated diffs and commits before merging, require the relevant quality gates to pass, and keep rollback available for failed fix loops. <br>
Risk: Real-backend testing and data seeding can affect the wrong environment if project configuration points at shared or production resources. <br>
Mitigation: Run against an isolated local or test environment with non-production credentials and data, and confirm backend, migration, and seed commands before autonomous execution. <br>


## Reference(s): <br>
- [Forge on ClawHub](https://clawhub.ai/ikennaokpala/skills/forge) <br>
- [Continuous Behavioral Verification: Ongoing Path to Done](https://www.linkedin.com/pulse/continuous-behavioral-verification-ongoing-path-done-ikenna-okpala) <br>
- [Build with Quality Skill: How I Build Software 10x Faster](https://www.linkedin.com/pulse/build-quality-skill-how-i-build-software-10x-faster-mondweep-chakravorty) <br>
- [claude-code-v3-qe-skill](https://github.com/mondweep/vibe-cast) <br>
- [agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with inline code, shell commands, JSON, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file edits, commands, tests, commits, and local configuration based on the target project.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact CHANGELOG.md, released 2026-02-07) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
