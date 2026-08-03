## Description: <br>
Manages fix_plan.md and checklist.md schemas, lifecycle transitions, priority triage, sync checks, issue drafts, model-triage sections, completion criteria, and flowchart drift checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and project maintainers use this skill to keep work trackers structured, synchronize GitHub-backed work states, triage blocked items, preserve completion history, and record deferred plan or issue-draft work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit and archive fix_plan.md or checklist.md content, which can change tracker state and move completion history. <br>
Mitigation: Use it only in workspaces where tracker maintenance is intended, review diffs after runs, and prefer dry-run or preview modes when using bundled cleanup helpers. <br>
Risk: Bundled Plane helpers and workspace profile resolution can access configured Plane credentials; workspace_profile.py --json may expose token values in command output. <br>
Mitigation: Avoid running workspace_profile.py --json with real credentials until output is redacted, and use least-privilege Plane API keys in controlled environments. <br>
Risk: Qdrant pre-lookup and post-ingest helpers can query or index markdown artifacts and local wiki content into configured collections. <br>
Mitigation: Disable or remove the Qdrant helpers unless semantic indexing is explicitly desired, and verify workspace-specific collections before indexing sensitive documents. <br>
Risk: GitHub synchronization relies on gh CLI state polling; failed or stale API checks can leave tracker items unresolved. <br>
Mitigation: Treat sync reports as reviewable status, leave uncertain API results unchanged, and re-run sync after credentials, repository access, or network issues are fixed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/fix-plan) <br>
- [Fix Plan Skill Definition](SKILL.md) <br>
- [Format Guide](format.md) <br>
- [Priority Guide](priority.md) <br>
- [Sync Guide](sync.md) <br>
- [Move Guide](move.md) <br>
- [Completion Criteria Guide](completion-criteria.md) <br>
- [Model Triage Guide](model-triage.md) <br>
- [Flowchart Guide](flowchart.md) <br>
- [Issue Drafts Guide](issue-drafts.md) <br>
- [Release Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tracker edits, concise run reports, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May edit tracker files, create archive files under .bak, run gh commands, and use optional helper scripts for Plane connectivity and Qdrant lookup or indexing.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
