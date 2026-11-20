## Description:

Convert a Markdown article into an HTML fragment Medium's story editor accepts on paste.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to prepare Markdown articles for pasting into Medium while retaining supported formatting and multi-line code. It reports the title separately and prepares hosted images or table images for the article.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review classifies this skill as suspicious: reported image-readiness behavior is inconsistent, Chromium table rendering is reported without sandboxing, and scan coverage is partial because referenced paths were missing.

Mitigation: Review the security findings and complete scan coverage before installation. Reconcile image-readiness behavior and use sandboxed browser rendering for untrusted Markdown tables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/md-to-medium)

## Skill Output:

**Output Type(s):** [HTML, Text, Files, Guidance]

**Output Format:** [An HTML fragment and a plain-text conversion status report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The HTML is saved beside the source article by default; the title is reported separately. Tables can be represented as hosted PNGs or bullet lists.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
