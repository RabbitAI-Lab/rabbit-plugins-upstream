## Description: <br>
Quaderno helps agents operate Quaderno through an OOMOL-connected account to read tax, account, contact, and product data and to create, update, or delete contacts and products. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage Quaderno tax, account, contact, and product workflows through an OOMOL-connected account. It guides agents to inspect the live connector schema before building payloads and to confirm state-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quaderno operations may touch business and financial records, including customer, tax, payment, cancellation, and delete operations. <br>
Mitigation: Treat these operations as sensitive and require explicit user confirmation before changing business or financial records. <br>
Risk: Write actions can change Quaderno contacts or products, and destructive actions can permanently delete contacts or products. <br>
Mitigation: Confirm the exact payload, target record, and expected effect with the user before running write or destructive actions. <br>
Risk: Connector schemas can define required fields and response shapes that are not known until runtime. <br>
Mitigation: Inspect the live action schema before constructing a payload and use the schema as the authority for inputs. <br>


## Reference(s): <br>
- [Quaderno homepage](https://quaderno.io/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quaderno) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Quaderno connector commands and JSON payloads; write and destructive actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
