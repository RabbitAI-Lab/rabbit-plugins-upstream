## Description: <br>
Migrates a WeChat Mini Program from the Skyline renderer to WebView while preserving visual and behavioral consistency through a deterministic scan, a MIGRATION-MAP, and targeted verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to migrate WeChat Mini Programs off Skyline and onto WebView with minimal diffs. It produces a scan and MIGRATION-MAP before edits, flips renderer configuration, and guides page-by-page verification and targeted fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is expected to inspect and modify a local WeChat Mini Program migration branch, including renderer configuration and possible page fixes. <br>
Mitigation: Run it on a clean git working tree, generate the MIGRATION-MAP before edits, review the planned changes, and use the documented rollback path for app.json and touched page JSON files. <br>
Risk: Skyline-only features can break under WebView if they are silently dropped or treated as simple compatibility workarounds. <br>
Mitigation: Treat rewrite findings as a manual-review gate, surface them before edits, and do not silently remove or replace hard Skyline-only behavior. <br>
Risk: Visual or behavioral regressions may be missed if runtime verification is incomplete. <br>
Mitigation: Capture before/after screenshots and pageData for each relevant page with vince-mp, treat snapshot timeouts as blockers, and apply only fixes tied to confirmed deltas. <br>


## Reference(s): <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Scan protocol](artifact/rules/scan-protocol.md) <br>
- [Verify with vince-mp](artifact/rules/verify-with-vince-mp.md) <br>
- [Minimal-fix protocol](artifact/rules/minimal-fix-protocol.md) <br>
- [Scanner contract](artifact/references/scanner-contract.md) <br>
- [Skyline to WebView mapping](artifact/references/skyline-to-webview.md) <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/mp-groundline) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, shell commands, configuration edits, and concise implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a MIGRATION-MAP, scan results, renderer configuration changes, targeted code or style fixes, and rollback-oriented status reporting.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
