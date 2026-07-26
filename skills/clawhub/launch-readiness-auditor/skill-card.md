## Description: <br>
Audits one launch at one declared RAMP lifecycle read: preflight readiness, launch-window execution, or post-lag outcome review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Launch teams and marketing operators use this skill to evaluate go/no-go readiness, observed execution quality, or outcome proof for a single launch without mixing lifecycle horizons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reviews launch plans, claims, rules, analytics, and web sources that may include sensitive launch evidence. <br>
Mitigation: Provide only the evidence needed for the selected lifecycle read and avoid sharing unrelated confidential launch materials. <br>
Risk: Audit output could be mistaken for permission to launch or mutate launch records. <br>
Mitigation: Treat the result as review guidance only; require separate authorization for launch execution, registry mutation, or artifact persistence. <br>
Risk: Standalone installs may lack the deterministic scorer and validator needed for authoritative scoring. <br>
Mitigation: When the required runtime is unavailable, return not-scored status and do not hand-calculate a substitute gate verdict. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/launch-readiness-auditor) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Standalone Auditor Runtime](artifact/references/auditor-runtime.md) <br>
- [Distribution Manifest](artifact/distribution-manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown audit report with explicit status, verdict, score state, unknowns, and evidence-linked findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose deterministic scoring commands when a full repository runtime is available; standalone fallback must not compute substitute scores or persist artifacts without authorization.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
