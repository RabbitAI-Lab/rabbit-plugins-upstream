## Description:

Use when a US medical bill, Explanation of Benefits, or collections notice arrives and the numbers make no sense. Decodes CPT/HCPCS/revenue codes, reconstructs the allowed-amount chain (charge → contractual writeoff → insurance payment → patient share), finds upcoding and duplicate-charge patterns, and generates an itemized-bill request + dispute letter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Patients and caregivers use the skill to review US medical bills, EOBs, and collections notices, compare billed, allowed, paid, and patient-share amounts, and prepare itemized-bill requests or dispute letters.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Bills and EOBs can contain sensitive personal information.

Mitigation: Provide only the bill details needed for review and consider the agent's privacy settings.

Risk: The script ignores service dates, and the documented --eob option is absent; audit flags may therefore miss relevant context.

Mitigation: Check service dates and reconcile each result directly against the itemized bill, EOB, and plan documents.

Risk: Draft dispute claims are not verified outcomes or a determination that a charge is incorrect.

Mitigation: Review and substantiate every flag and letter before sending; do not treat confident wording as proof of a successful dispute.

## Reference(s):

- [Medical Bill Decoding — Full Reference](references/decoding-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Plain-text audit findings and drafted letters, with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review findings against the bill, EOB, and plan documents before acting.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
