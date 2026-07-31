## Description: <br>
Autonomous orchestrator for manifest work items through the development lifecycle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use Summon to run manifest-backed work items through intake, build, quality, and shipping stages by delegating each pipeline step to specialist skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate unattended and continue without asking for clarification. <br>
Mitigation: Use bounded mode for normal runs and review the manifest, branches, and pull requests before accepting changes. <br>
Risk: The skill can change repository state, create branches or pull requests, and optionally merge changes. <br>
Mitigation: Disable auto-merge unless explicitly required and keep human review in the pull request workflow. <br>
Risk: The skill can use GitHub issue content and prompts while orchestrating work. <br>
Mitigation: Avoid including secrets or sensitive data in prompts, issue bodies, and issue comments used as work-item input. <br>
Risk: The skill can schedule resume prompts or recurring heartbeat tasks. <br>
Mitigation: Review scheduled tasks during setup and delete any cron heartbeat when the orchestration run is finished. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-summon) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, configuration examples, and state-management instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Delegates work to configured specialist skills and may update repository state, manifests, branches, pull requests, and scheduled resume prompts.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
