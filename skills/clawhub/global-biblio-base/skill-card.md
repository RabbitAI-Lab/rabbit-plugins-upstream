## Description:

Provides SmartLib-powered Chinese and global academic literature search, literature details, source-link display, citation-oriented ranking, and authorized or open-access PDF retrieval for research workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers use this skill to search Chinese and global scholarly literature, inspect metadata and source links, and retrieve authorized Chinese journal PDFs or openly available international PDFs when they have rights to use them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user email addresses, search requests, document identifiers, and payment-order details through SmartLib and Alipay-related flows.

Mitigation: Use the skill only after the user knowingly provides an email address, disclose email use before payment order creation, and avoid submitting unnecessary personal or sensitive information.

Risk: The skill can initiate paid quota or download-plan flows after quota exhaustion or a user upgrade request.

Mitigation: Require deliberate plan selection, verify the plan price and order details before payment, and do not treat payment as complete until the payment status endpoint confirms success.

Risk: The automated PDF retrieval path includes broad open-access lookup and anti-hotlink workaround behavior.

Mitigation: Run full-text retrieval only after an explicit user request, limit use to authorized Chinese journal downloads or clearly open-access sources, and stop or redirect users when content is closed access.

Risk: The skill depends on gateway credentials and networked API access.

Mitigation: Keep gateway secrets out of conversation output and generated payment pages, review the skill before installation, and verify where downloaded files will be written.

## Reference(s):

- [SmartLib account and billing](references/account.md)
- [SmartLib payment page template](references/pay_page_template.html)
- [SmartLib pipeline guide](PIPELINE.md)
- [Skill README](README.md)
- [VIP Smart official website](https://www.vipslib.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown search results and reports, JSON API request bodies, payment HTML when initiated, and PDF download links or file references when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include quota status, source database links, payment-plan choices, masked payment email, and retrieval status labels for full-text attempts.]

## Skill Version(s):

3.10.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
