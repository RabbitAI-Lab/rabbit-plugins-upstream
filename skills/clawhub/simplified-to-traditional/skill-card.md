## Description:

Convert a Simplified-Chinese article in ai-thoughts/docs/ into its Traditional-Chinese twin, and keep the two in sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use it to convert an explicitly named Simplified-Chinese article into a Traditional-Chinese counterpart and keep the two files cross-linked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversion may alter wording or choose an incorrect Traditional-Chinese form, especially in quotations.

Mitigation: Review the converted article for accuracy and verify quoted text against its cited edition before approving it.

Risk: The sync script can overwrite a Traditional-Chinese file and insert permanent cross-links without prompting.

Mitigation: Review both files and preserve existing translations before approving an overwrite; verify the links and installation path.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/simplified-to-traditional)

## Skill Output:

**Output Type(s):** [Files, Markdown]

**Output Format:** [Traditional-Chinese Markdown article with a cross-link to its Simplified-Chinese source]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OpenCC s2twp conversion; acts only on an explicitly named article after approval.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
