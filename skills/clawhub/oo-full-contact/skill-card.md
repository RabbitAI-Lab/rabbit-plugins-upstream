## Description: <br>
FullContact (fullcontact.com). Use this skill for FullContact requests involving search, enrichment, verification, and reading data through the OOMOL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run FullContact company enrichment, person enrichment, and identity verification through an OOMOL-connected FullContact account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Person enrichment and verification can involve sensitive personal identifiers. <br>
Mitigation: Run only lookups the user explicitly requested and avoid sending unnecessary identifiers. <br>
Risk: OOMOL or FullContact billing and account policies may apply. <br>
Mitigation: Confirm the connected account and expected cost context before repeated or large lookups. <br>


## Reference(s): <br>
- [FullContact homepage](https://www.fullcontact.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub FullContact skill page](https://clawhub.ai/oomol/skills/oo-full-contact) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands inspect the live connector schema before running FullContact actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
