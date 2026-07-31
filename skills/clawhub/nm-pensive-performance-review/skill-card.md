## Description: <br>
Detects time and space complexity hotspots via AST scan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before performance-sensitive merges or during triage to identify likely time and space complexity hotspots in code. It produces severity-ranked findings and suggestions that should be confirmed with profiling or benchmarks before changes are treated as proven fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Static analysis findings can be false positives or may not represent a real runtime bottleneck. <br>
Mitigation: Confirm important findings with profiling, benchmarks, and manual sampling before treating a proposed fix as proven. <br>
Risk: Optional gauntlet and kuva integrations broaden the tool surface used during analysis and reporting. <br>
Mitigation: Review and install those separate tools only when multi-language, call-graph, or charting support is needed. <br>
Risk: The skill reads target code supplied for review. <br>
Mitigation: Use it only on code the agent is authorized to inspect and follow local handling rules for sensitive repositories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-performance-review) <br>
- [Pensive homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [kuva plotting library](https://github.com/Psy-Fer/kuva) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown report with severity-ranked findings, concrete suggestions, and optional code or shell snippets for verification and charting.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports Tier 1 Python AST coverage by default; optional gauntlet support can add multi-language and call-graph enrichment when available.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
