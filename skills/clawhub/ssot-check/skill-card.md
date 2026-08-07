## Description: <br>
SSOT Check audits documentation-heavy repositories for hand-copied facts, helps build a `.ssot.yaml` manifest of canonical values and copies, and checks whether those copies still match. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use SSOT Check to discover duplicated facts in documentation, propose a single-source-of-truth manifest, and check for stale copies before documentation changes are committed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may propose an incorrect canonical source or stale-copy fix when documentation facts are ambiguous. <br>
Mitigation: Review proposed `.ssot.yaml` entries and diffs before approving any writes. <br>
Risk: Cross-repo checks can be unverifiable when sibling clones or remote-tracking refs are unavailable or stale. <br>
Mitigation: Report those facts as UNVERIFIED unless the user explicitly requests a live remote fetch for that session. <br>
Risk: A live remote fetch in a sibling clone writes remote-tracking refs and related Git metadata. <br>
Mitigation: Treat live fetches as explicit per-session actions and name the sibling repo before fetching. <br>


## Reference(s): <br>
- [SSOT Check README](README.md) <br>
- [Discovery Prompt Pattern](patterns/discovery-prompt.md) <br>
- [Worked Discovery Report](examples/cot-production-discovery/discovery-report.md) <br>
- [Proposed SSOT Manifest Example](examples/cot-production-discovery/proposed-ssot.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown reports with YAML manifest proposals, diffs, and inline shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-oriented by default; proposes `.ssot.yaml` entries and content diffs for human approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
