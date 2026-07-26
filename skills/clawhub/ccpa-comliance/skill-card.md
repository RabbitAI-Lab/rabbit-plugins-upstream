## Description: <br>
CCPA-Compliance helps teams assess CCPA/CPRA obligations, check consumer-rights and opt-out workflows, and generate draft compliance reports for businesses handling California consumer data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, compliance teams, and business operators use this skill to run local CCPA/CPRA self-checks, review consumer-rights and opt-out processes, and produce draft JSON, Markdown, HTML, CSV, or text reports. Its outputs are compliance aids and must not be treated as legal advice. <br>

### Deployment Geography for Use: <br>
United States (California consumer privacy workflows); globally usable by teams assessing California-facing data practices. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate legal or compliance guidance that may be outdated, incomplete, or not applicable to a specific business. <br>
Mitigation: Use outputs as draft checklists only, verify CCPA/CPRA thresholds and obligations against official sources, and consult qualified counsel before business or regulatory decisions. <br>
Risk: Local scripts may execute commands or inspect local files during checks. <br>
Mitigation: Review the Python scripts before running them, especially security_check_ccpa.py, and run them in a controlled local workspace. <br>
Risk: Reports may contain sensitive business or privacy assessment details. <br>
Mitigation: Store generated reports in approved locations, limit sharing, and remove sensitive details before distribution. <br>


## Reference(s): <br>
- [CCPA/CPRA summary guide](references/ccpa-law.md) <br>
- [Security check and running guide](SECURITY_CHECK_GUIDE.md) <br>
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ccpa-comliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [CLI guidance and local audit reports in text, JSON, Markdown, HTML, or CSV] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python standard library scripts; legal outputs require human review.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
