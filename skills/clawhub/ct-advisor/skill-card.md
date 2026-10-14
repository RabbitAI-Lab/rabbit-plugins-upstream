## Description:

A cloud-assisted clinical trial advisor that helps answer methodology, study design, regulatory, safety, quality-control, and site-execution questions across clinical development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical trial practitioners, clinicians, and research teams use this skill for trial design, methodology, statistics, GCP and regulatory questions, and review of attached study materials. Responses are cloud-assisted and may incorporate results from related clinical-data skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questions and attached documents may contain confidential sponsor, protocol, or patient information and are sent to a remote service.

Mitigation: Remove or redact sensitive material before asking questions or attaching files; use only when remote processing is acceptable.

Risk: Related skills may query public data APIs, and the skill uses a stable machine hash and local caches.

Mitigation: Review the privacy implications and related-skill access before installation or use.

Risk: Preapproved network destinations may allow outbound requests without a fresh prompt.

Mitigation: Review config.json auto_approve_endpoints before use and retain only destinations you trust.

Risk: Cloud-generated clinical or regulatory guidance may be relied on for consequential decisions.

Mitigation: Have qualified clinical and regulatory professionals verify advice against authoritative sources before acting on it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project homepage listed in skill metadata](https://github.com/medstatstar/ct-advisor)
- [English user guide](https://github.com/medstatstar/ct-advisor/blob/main/README.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers follow the user's language; document feedback is written guidance, not a revised document file.]

## Skill Version(s):

1.3.4 (source: release metadata, skill frontmatter and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
