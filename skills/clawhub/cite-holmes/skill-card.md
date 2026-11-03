## Description:

Supports deep research and reference checking by gathering literature, checking citation records, and producing research reports and bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Researchers, students, and research assistants can use this skill to discover literature, check citation records and retraction signals, and prepare reports and bibliography exports. Treat its results as a review aid and independently check citations before relying on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed flaws may bypass network restrictions and make unreliable citations appear verified.

Mitigation: Enforce network controls independently, including blocking private destinations; independently check citations, retraction status, and exports before relying on results.

Risk: Transmission and credential handling issues may expose submitted research inputs or optional API credentials.

Mitigation: Avoid confidential inputs and valuable API keys until transmission and credential handling are corrected.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Publisher profile](https://clawhub.ai/user/docsor1212)
- [Security and behavior declaration](references/security.md)
- [Citation verification limits](references/out-of-scope.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, CSV, BibTeX, RIS, GB/T 7714 text]

**Output Format:** [Research and verification reports, structured audit workpapers, and bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include citation verdicts and human-review flags; verification does not establish that a cited source supports a claim.]

## Skill Version(s):

5.9.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
