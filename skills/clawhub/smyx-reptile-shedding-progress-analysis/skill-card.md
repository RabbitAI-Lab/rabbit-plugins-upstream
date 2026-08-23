## Description:

Analyzes reptile enclosure images or videos to classify shedding phase, detect visible stuck-shed risk signals, and produce care recommendations and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, vivarium operators, breeding farms, and developers integrating smart enclosure cameras use this skill to monitor reptile shedding progress from media inputs and receive structured phase classifications, risk flags, care suggestions, and history-report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud processing of reptile media and identity-bearing requests may expose media, report history, or account-linked activity outside the local environment.

Mitigation: Before use, confirm lifeemergence.com data retention, access, revocation, and deletion practices, and restrict URL analysis to trusted sources where possible.

Risk: The skill can create or reuse a backend-linked identity and store tokens locally with limited user control.

Mitigation: Review identity creation, token storage, and account lifecycle behavior before deployment, and document how users can revoke access or delete history.

Risk: Visual shedding guidance could be mistaken for veterinary diagnosis or invasive treatment advice.

Mitigation: Keep outputs limited to visual phase classification and non-invasive care suggestions, include disclaimers, and escalate persistent or high-risk stuck-shed findings to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include shedding phase, alert level, visible risk zones, recommended actions, disclaimers, saved result files, and historical report tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
